
import fresh_tomatoes
import media
import test_web_server


""" 调试时使用 """
debug = 0;


if __name__ == "__main__":

	movies = [
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924"),
		media.Movie("艳骨", "XMzA5NzkxNTYzMg", "051000005A46D826ADC0AE078B010924")
	];


	if debug:
		content = fresh_tomatoes.create_page_content(movies);
		test_web_server.start("192.168.56.101",4780,content);
	else:
		fresh_tomatoes.open_movies_page(movies);
		
