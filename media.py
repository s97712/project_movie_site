
""" 构造生成html所需要的movie结构 """
class Movie:
	"""
	Args:
		title:	电影的标题
		id:		优酷视频的show_id
		image:	优酷的图片id

	"""

	def __init__(self, title, id, image):
		self.title = title;	
		self.trailer_url = "http://v.youku.com/v_show/id_"+ id+ "==.html?";
		self.poster_image_url = "http://r1.ykimg.com/" + image;
	
