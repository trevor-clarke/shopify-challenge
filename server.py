import tornado.web
import tornado.httpserver
import Database

connection = Database.Database()
web = tornado.web
handler = web.RequestHandler

print(connection.select_all()[0])
print()

class MainHandler(handler):
    def get(self):
        self.redirect("/photos")

class SecureRedirect(handler):
    def prepare(self):
        self.redirect("https://sketchthis.ca" + self.request.path)

class PageNotFound(handler):
    def prepare(self):
        self.write("The requested resource is not available. 404")


def dict_to_list(dict):
    return [dict[key] for key in dict.keys()]

def render_gallery_page(self, dict_images):
    cat_text = connection.select_distinct("category")
    categories = [[x, "/photos/query/category/" +x] for x in cat_text]
    #Tornado template doesn't support dicts in their html markup, convert to list:
    images = [dict_to_list(img) for img in dict_images]
    self.render("display_images.html",
                title="Trevor's Image Repo",
                categories=categories,
                images = images)

class PhotosHandler(handler):
    def get(self):
        render_gallery_page(self, connection.select_all())


class PhotosFeatureHandler(handler):
    def get(self, url_args):
        #validate the given args make sure they follow required format
        args = url_args.split("/")
        valid_arg_0 = ["query"]
        if len(args) == 3:
            if args[0] in valid_arg_0:
                #here we just have one call type 'query', but more could be added here
                if args[0] == valid_arg_0[0]:
                    results = connection.select_where(args[1], args[2])
                    if len(results) > 0:
                        render_gallery_page(self, results)
                    else:
                        #some js, for a quick redirect
                        self.write("<script>alert('No results found.');window.location.replace('/')</script>")
                    return
        self.redirect("/")

if __name__ == "__main__":
    app = web.Application([
            (r"/", MainHandler),
            (r"/photos", PhotosHandler),
            (r"/photos/(.*)", PhotosFeatureHandler),
            (r"/images/(.*)", web.StaticFileHandler, {"path": "public/images/"}),
        ], default_handler_class=PageNotFound, debug=True)

    #If you want to add an SSL Cert to the Server....
    ## UNCOMMENT THIS PART:

    # catcher = web.Application([(r"(.*)", SecureRedirect)])
    # server = tornado.httpserver.HTTPServer(app, ssl_options={
    #     "certfile": "[PATH TO CERTFILE]",
    #     "keyfile": "[PATH TO KEYFILE]"
    # })
    # catcher.listen(80)
    # server.listen(443)

    # AND COMMENT THIS PART
    server = tornado.httpserver.HTTPServer(app)
    server.listen(80)


    print("Server has started.")
    tornado.ioloop.IOLoop.instance().start()
