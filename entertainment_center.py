
import fresh_tomatoes
import media
import test_web_server		#简陋的web服务器


debug = 0;
""" 调试时使用，因为我是ssh环境，无法打开浏览器，所以通过一个简陋的web服务器来调试。
	debug = 1 打开调试，使用web服务器
	debug = 0 关闭调试，使用浏览器
"""


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
		test_web_server.start("0.0.0.0",4780,content);
	else:
		fresh_tomatoes.open_movies_page(movies);
		
