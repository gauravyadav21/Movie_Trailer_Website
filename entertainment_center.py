import media
import fresh_tomatoes

#Creating instance of Movie class that takes 4 arguments - title, description, image URL
# and web URL
kaabil = media.Movie("Kaabil",
		     "story of a blind man taking revenge of his wife dead",
		     "http://www.lyricsted.com/wp-content/uploads/2016/12/kaabil-hoon-lyrics-title-song-hrithik-roshan-yami-gautam.jpg",
		     "https://www.youtube.com/watch?v=nubDFeiUAsI")

dangal = media.Movie("Dangal",
		     "Former wrestler Mahavir Singh Phogat (Aamir Khan) trains young daughters Geeta (Fatima Sana Shaikh) and Babita (Sanya Malhotra) to follow in his footsteps and become world-class grapplers.",
		     "http://www.asianjournal.ca/wp-content/uploads/2016/12/Dangal.jpg",
		     "https://www.youtube.com/watch?v=x_7YlGv9u1g")


jolly_ll2 = media.Movie("Jolly llb 2",
		     "An ambitious lawyer (Akshay Kumar) finds himself in a battle with a ruthless advocate after making an innocent mistake.",
		     "http://st1.bollywoodlife.com/wp-content/uploads/2017/02/jolly-llb-2-1.jpg",
		     "https://www.youtube.com/watch?v=q07SQFmL4rM")

KFY = media.Movie("Kung Fu Yoga",
		     "Jack (Jackie Chan), a world-renowned archaeology professor, and his team are on a grand quest to locate a lost ancient Indian treasure when they are ambushed by a team of mercenaries.",
		     "http://t1.gstatic.com/images?q=tbn:ANd9GcSTH4JAXX6MleUJZNeew9pLomm0Y0Xa6WjJMTz-jgFCgu3z9tQj",
		     "https://www.youtube.com/watch?v=5KcwjfPdFC0")

raees = media.Movie("Raees",
		     "A determined police officer (Nawazuddin Siddiqui) threatens to destroy a crime lord's (Shah Rukh Khan) powerful empire in Gujarat, India.",
		     "http://t0.gstatic.com/images?q=tbn:ANd9GcTnNTLek-7L5YTgki1AQ3dBBxW5cqPonNI8uDSJPydwM-KJXPzr",
		     "https://www.youtube.com/watch?v=J7_1MU3gDk0")

BKD = media.Movie("Badrinath Ki Dulhania",
		     "A man (Varun Dhawan) and a woman (Alia Bhatt) fall in love despite their opposing views on gender and life in general.",
		     "http://t0.gstatic.com/images?q=tbn:ANd9GcRJSU1unyu9808UseNph0ICnjZhu6Zp7uzhL68_QWMgvclHgDPW",
		     "https://www.youtube.com/watch?v=ztX-iGlZ_Ug")

WTH = media.Movie("Wajah Tum Ho",
		     "The film revolves around a live murder committed on television.",
		     "http://songsmp3.co/assets/images/1/36316-Wajah%20Tum%20Ho%20(2016).jpg",
		     "https://www.youtube.com/watch?v=nubDFeiUAsI")

befikre = media.Movie("Befikre",
		     "Romantic comedy drama film.",
		     "http://t1.gstatic.com/images?q=tbn:ANd9GcTgd7bcKGy4_1BN2n6eZHUUC3jnATg5tOlrRypnjuRQgycHqwSl",
		     "https://www.youtube.com/watch?v=p7X7mwcEJ-w")

ADHM = media.Movie("Ae Dil Hai Mushkil",
		     "Musician Ayan's quest for true love remains unfulfilled as Alizeh doesn't reciprocate his feelings. In his journey, he comes across different people who make him realise the power of unrequited love.",
		     "http://t2.gstatic.com/images?q=tbn:ANd9GcS0oOG1QBwIczzDEZjZ6OmFIvthTiGGWI6PajZ_3s-SsBjavWVc",
		     "https://www.youtube.com/watch?v=Z_PODraXg4E")

movies = [kaabil, dangal, jolly_ll2, KFY, raees, BKD, WTH, befikre, ADHM]
fresh_tomatoes.open_movies_page(movies)
