import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

blade_runner = media.Movie("Blade Runner",
                           "Special police operatives known as 'Blade Runners' hunt rogue genetically engineered replicants that are indistinguishable from humans",
                           "http://www.impawards.com/1982/posters/blade_runner_xlg.jpg",
                           "https://www.youtube.com/watch?v=iYhJ7Mf2Oxs")

school_of_rock = media.Movie("School of Rock",
                             "A struggling musician teaches music to repressed private school preteens.",
                             "http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

stardust = media.Movie("Stardust",
                       "A young man chases a star into a world of magic and finds love",
                       "https://images-na.ssl-images-amazon.com/images/I/51eV9jsY0JL.jpg",
                       "https://www.youtube.com/watch?v=83XRTl_JE1o")

la_la_land = media.Movie("La La Land",
                         "A struggling actress falls in love with a determined jazz pianist.",
                         "https://www.cinematerial.com/media/posters/md/xr/xrj85wlh.jpg?v=1480379694",
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

prometheus = media.Movie("Prometheus",
                         "An archeaologist follows a map found on Earth to a distant planet.",
                         "https://s-media-cache-ak0.pinimg.com/originals/25/1c/16/251c16afa4ef068477726b5092eecbe5.jpg",
                         "https://www.youtube.com/watch?v=sftuxbvGwiU")

chinatown = media.Movie("Chinatown",
                        "1937 Los Angeles hard-boiled detective story concerning water rights.",
                        "https://images-na.ssl-images-amazon.com/images/I/81%2BebrESqBL._SY450_.jpg",
                        "https://www.youtube.com/watch?v=2yJJWXhXbuI")

movies = [toy_story,
          avatar,
          blade_runner,
          school_of_rock,
          stardust,
          la_la_land,
          prometheus,
          chinatown]

fresh_tomatoes.open_movies_page(movies)
