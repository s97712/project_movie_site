
# Movie结构
# {
#	trailer_url
#	title
#	poster_image_url
# }


class Movie:
	def __init__(self, title, id, image):
		self.title = title;
		self.trailer_url = "http://v.youku.com/v_show/id_"+ id+ "==.html?";
		#self.trailer_url = "http://v.youku.com/v_show/id_" + id;
		self.poster_image_url = "http://r1.ykimg.com/" + image;


def generate_movies():
	movies = [];
	movie = Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924");
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	movies.append(movie);
	return movies;
