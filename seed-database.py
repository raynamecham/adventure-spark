"""Script to seed database."""
import os
import crud
import model
import server

os.system('dropdb adventurespark')
os.system('createdb adventurespark')

model.connect_to_db(server.app)
model.db.create_all()

crud.create_user('admin', 'admin@admin.com', 'admin')

crud.create_location('Paris', 48.8620605, 2.2958039, "The City of Light draws millions of visitors every year with its unforgettable ambiance.")
crud.create_location('Bora Bora', -16.499701, -151.770538, "What this small island may lack in size it makes up for in sheer tropical beauty. Here, you'll find picturesque beaches, lush jungles and luxurious resorts.")
crud.create_location('South Island, New Zealand', -40.923859, 173.991425, "New Zealand's South Island brims with majestic landscapes at every turn, from dramatic mountains to fjords to glaciers.")
crud.create_location('Glacier National Park', 48.502281, -113.988533, "Snow-capped peaks and azure lakes are just two reasons why Glacier National Park is one of the most-visited parks in the United States. ")
crud.create_location('London', 51.507351, -0.127758, "London is a world unto itself. The eclectic neighborhoods, which house a blend of historical landmarks and modern-day attractions, can keep you occupied for days.")
crud.create_location('Maui', 20.798363, -156.331924, "Whether you're driving along the Road to Hana, enjoying a bird's-eye view of the lush coastline from a helicopter, snorkeling with sea turtles or simply relaxing on the island's honey- or black-colored beaches, you'll find that Maui is unlike any other tropical destination. ")
crud.create_location('Tahiti', -17.650921, -149.426041, "Travel to this island – the largest in French Polynesia – if you've been dreaming of a vacation spent lazing in a lavish overwater bungalow. ")
crud.create_location('Tokyo', 35.689487, 139.691711, "Simply setting foot in Japan's cosmopolitan capital is an experience within itself. A city known for its bustling streets adorned with flashing neon signs, Tokyo offers visitors a little bit of everything.")
crud.create_location('Phuket', 7.951933, 98.338089, "Located in southern Thailand, Phuket offers something for everyone, especially budget-minded travelers. Everything from accommodations to spa treatments to boat tours come with a low price tag.")
crud.create_location('Barcelona', 41.385063, 2.173404, "This Spanish city is a feast for the eyes: Visitors can walk past medieval architecture in the Barri Gòtic, snap photos of the intricate Sagrada Família and marvel at Gaudí's whimsical creations in Park Güell.")
crud.create_location('Bali', -8.340539, 115.091949, "Serene temples and beautiful beaches are the biggest draws to this lush Indonesian paradise. ")
crud.create_location('New York City', 40.712776, -74.005974, "New York City hosts infinite urban adventures: You can wander through Central Park, tour the exhibits at the Met, catch a Broadway show or peruse SoHo's stylish boutiques.")
crud.create_location('Grand Canyon', 36.106964, -112.112999, "Measuring roughly 277 miles long, 18 miles wide and a mile deep, the Grand Canyon offers plenty of outdoor activities for everyone from day-trippers to adventure junkies.")
crud.create_location('Dubai', 25.204849, 55.270782, "Stunning Persian Gulf views, heart-pumping activities and historical landmarks await you in Dubai.")
crud.create_location('Machu Picchu', -13.163141, -72.544960, "A visit to the 'Lost City of the Incas' is not for the faint of heart, but it is often described as life-changing (once you acclimate to the altitude).")
crud.create_location('Sydney', -33.868820, 151.209290, "This Australian city boasts a warm, sunny climate that is ideal for relaxing or surfing at world-renowned beaches like Coogee, Bondi and Manly.")
crud.create_location('Banff', 51.178509, -115.574280, "An Alberta town full of acclaimed restaurants, breweries, boutiques and art galleries, Banff makes for an exciting vacation in every season. ")
crud.create_location('Florence', 43.769562, 11.255814, "Florence offers plenty of world-famous attractions, including the Duomo, Piazzale Michelangelo and Piazza della Signoria.")
crud.create_location('Yosemite', 37.865101, -119.538330, "Year after year, millions of visitors travel to California's Yosemite National Park to stand in awe of natural wonders like Half Dome and Yosemite Falls. ")
crud.create_location('Santorini', 36.393154, 25.461510, "Frequently touted as a top honeymoon destination, this Greek isle woos newlyweds every year with its breathtaking sunsets, pastel-hued villages and colorful beaches. ")
crud.create_location('Yellowstone', 44.427963, -110.588455, "Considered by many to be a rite of passage for any American, a visit to this national park in Idaho, Montana and Wyoming will leave you in awe of nature's power.")
crud.create_location('St. Lucia', 13.9095248, -60.9763851, "Dotted with luxurious boutique hotels, this Caribbean destination is tailor-made for lovebirds and adrenaline junkies.")
crud.create_location('Great Barrier Reef', -16.601959, 145.522751, "The globe's largest coral reef system – and one of the original Seven Natural Wonders of the World – touts incredible scenery, whether you view it underwater, from the air or by boat.")
crud.create_location('San Francisco', 37.774929, -122.419418, "Home to some of America's most recognizable landmarks – including the Golden Gate Bridge, Fisherman's Wharf and Alcatraz Island – San Francisco has the ability to satisfy outdoorsy types, foodies and curious wanderers of all ages. ")
crud.create_location('Amsterdam', 52.370216, 4.895168, "Famous museums, tulips, canal-lined streets, coffee shops, and high-end boutiques await you in Amsterdam.")
crud.create_location('Rio de Janeiro', -22.906847, -43.172897, "Christ the Redeemer and the shores of Copacabana and Ipanema beaches are only some reasons why you should plan a trip to Rio.")
crud.create_location('Argentine Patagonia', -37.897280, -63.852400, "Argentine Patagonia is a must-visit destination if you consider yourself an adventurous traveler.")
crud.create_location('Costa Rica', 9.748917, -83.753426, "From volcanic mountains to verdant rainforests to stunning shorelines, Costa Rica is a Central American gem.")
crud.create_location('Niagara Falls', 43.096214, -79.037743, "A spectacular cluster of three waterfalls, Niagara Falls is a must-see if you want a glimpse of some of North America's best sites.")
crud.create_location('Seoul', 37.566536, 126.977966, "As the largest city in South Korea, this dynamic city is a bewitching mix of ancient and modern, packaged in a surprisingly compact metropolis.")
crud.create_location('Rome', 41.902782, 12.496365, "When you visit the Eternal City, prepare to cross a few must-see attractions – including the Colosseum, the Trevi Fountain and the Pantheon – off of your bucket list. ")

crud.create_adventure(1, 1)