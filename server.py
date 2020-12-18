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
    id_text = connection.select_distinct("id")

    categories = [[x, "/photos/query/category/" +x] for x in cat_text]
    ids = [[str(x), "/photos/query/id/" + str(x)] for x in id_text]
    #Tornado template doesn't support dicts in their html markup, convert to list:
    images = [dict_to_list(img) for img in dict_images]
    self.render("display_images.html",
                title="Trevor's Image Repo",
                categories=categories,
                ids=ids,
                images = images)

def image_not_found(self):
    self.write("<script>alert('No results found.');window.location.replace('/')</script>")


def render_single_photo_page(self, dict_image):
    #Tornado template doesn't support dicts in their html markup, convert to list:
    image = dict_to_list(dict_image)
    print("here", image)
    self.render("display_image.html",
                title="Trevor's Image Repo",
                image = image)


class SinglePhotoHandler(handler):
    def get(self, url_args):
        args = url_args.split("/")
        if len(args) == 1:
            results = connection.select_where("id", int(args[0]))
            if len(results) > 0:
                render_single_photo_page(self, results[0])
            else:
                image_not_found(self)
            return
        image_not_found(self)





class PhotosHandler(handler):
    def get(self):
        render_gallery_page(self, connection.select_all())

class PhotosFilterHandler(handler):
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
                        image_not_found(self)
                    return
        self.redirect("/")

if __name__ == "__main__":
    app = web.Application([
            (r"/", MainHandler),
            (r"/photo/(.*)", SinglePhotoHandler),
            (r"/photos", PhotosHandler),
            (r"/photos/(.*)", PhotosFilterHandler),
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
