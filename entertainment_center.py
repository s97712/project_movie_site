import fresh_tomatoes
import media
import test_web_server

movies = media.generate_movies();	#生成随机电影列表


debug = 1

if debug :
	content = fresh_tomatoes.create_movie_tiles_content(movies);
	content = "hello world";
	test_web_server.start("192.168.56.101",4780,content);
else:
	fresh_tomatoes.open_movies_page(movies);
	
	
	
