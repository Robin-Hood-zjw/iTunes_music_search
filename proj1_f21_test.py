import unittest
import json
import proj1_f21 as proj1

####################
###### Part 1 ######
####################

class TestMedia(unittest.TestCase):

	def testExample(self):
		m1 = proj1.Media("1999", "Prince")
		self.assertEqual(m1.title, "1999")
		self.assertEqual(m1.author, "Prince")

	def testConstructor(self):
		m1 = proj1.Media()
		m2 = proj1.Media("1999", "Prince", 1982, "https://www.example-url-1999.com")
		self.assertEqual(m1.title, "No Title")
		self.assertEqual(m1.author, "No Author")
		self.assertEqual(m1.release_year, "No Release Year")
		self.assertEqual(m2.title, "1999")
		self.assertEqual(m2.author, "Prince")
		self.assertEqual(m2.release_year, 1982)
		self.assertEqual(m2.url, "https://www.example-url-1999.com")
		self.assertRaises(AttributeError, lambda: m2.album)
		self.assertRaises(AttributeError, lambda: m2.genre)
		self.assertRaises(AttributeError, lambda: m2.track_length)
		self.assertRaises(AttributeError, lambda: m2.rating)
		self.assertRaises(AttributeError, lambda: m2.movie_length)

	def testInfo(self):
		m2 = proj1.Media("1999", "Prince", 1982)
		self.assertEqual(m2.info(), "1999 by Prince (1982)")

	def testLength(self):
		m2 = proj1.Media("1999", "Prince", 1982)
		self.assertEqual(m2.length(), 0)


class TestSong(unittest.TestCase):

	def testConstructor(self):
		s1 = proj1.Song()
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "https://www.example-url-havana.com", "Camila", "Pop", 216000)

		self.assertEqual(s1.album, "No Album")
		self.assertEqual(s1.track_length, 0)
		self.assertEqual(s2.title, "Havana")
		self.assertEqual(s2.author, "Camila Cabello")
		self.assertEqual(s2.release_year, 2018)
		self.assertEqual(s2.url, "https://www.example-url-havana.com")
		self.assertEqual(s2.album, "Camila")
		self.assertEqual(s2.genre, "Pop")
		self.assertEqual(s2.track_length, 216000)
		self.assertRaises(AttributeError, lambda: s2.rating)
		self.assertRaises(AttributeError, lambda: s2.movie_length)

	def testInfo(self):
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "https://www.example-url-havana.com", "Camila", "Pop", 216000)

		self.assertEqual(s2.info(), "Havana by Camila Cabello (2018) [Pop]")

	def testLength(self):	
		s2 = proj1.Song("Havana", "Camila Cabello", 2018, "https://www.example-url-havana.com", "Camila", "Pop", 216000)

		self.assertEqual(s2.length(), 216)


class TestMovie(unittest.TestCase):

	def testConstructor(self):
		m1 = proj1.Movie()
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "https://www.example-url-chorus.com", "PG-13", 5700000)

		self.assertEqual(m1.rating, "No Rating")
		self.assertEqual(m1.movie_length, 0)
		self.assertEqual(m2.title, "The Chorus")
		self.assertEqual(m2.author, "Christophe Barratier")
		self.assertEqual(m2.release_year, 2005)
		self.assertEqual(m2.url, "https://www.example-url-chorus.com")
		self.assertEqual(m2.rating,"PG-13")
		self.assertEqual(m2.movie_length, 5700000)
		self.assertRaises(AttributeError, lambda: m2.album)
		self.assertRaises(AttributeError, lambda: m2.genre)
		self.assertRaises(AttributeError, lambda: m2.track_length)

	def testInfo(self):
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "https://www.example-url-chorus.com", "PG-13", 5700000)

		self.assertEqual(m2.info(), "The Chorus by Christophe Barratier (2005) [PG-13]")

	def testLength(self):
		m2 = proj1.Movie("The Chorus", "Christophe Barratier", 2005, "https://www.example-url-chorus.com", "PG-13", 5700000)

		self.assertEqual(m2.length(), 95)

####################
###### Part 2 ######
####################

class TestJson(unittest.TestCase):
	
	def testMedia(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		m = proj1.Media(json=sample_data[2])

		self.assertEqual(m.title, "Bridget Jones's Diary (Unabridged)")
		self.assertEqual(m.author, "Helen Fielding")
		self.assertEqual(m.release_year, "2012")
		self.assertEqual(m.url, "https://itunes.apple.com/us/audiobook/bridget-joness-diary-unabridged/id516799841?uo=4")
		self.assertEqual(m.info(), "Bridget Jones's Diary (Unabridged) by Helen Fielding (2012)")
		self.assertEqual(m.length(), 0)

	def testSong(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		s = proj1.Song(json=sample_data[1])
		
		self.assertEqual(s.title, "Hey Jude")
		self.assertEqual(s.author, "The Beatles")
		self.assertEqual(s.release_year, "1968")
		self.assertEqual(s.url, "https://itunes.apple.com/us/album/hey-jude/400835735?i=400835962&uo=4")
		self.assertEqual(s.album, "TheBeatles 1967-1970 (The Blue Album)")
		self.assertEqual(s.genre, "Rock")
		self.assertEqual(s.track_length, 431333)
		self.assertEqual(s.info(), "Hey Jude by The Beatles (1968) [Rock]")
		self.assertEqual(s.length(), 431)

	def testMovie(self):
		f = open("sample_json.json","r")
		sample_data = json.loads(f.read())
		f.close()
		
		m = proj1.Movie(json=sample_data[0])
		
		self.assertEqual(m.title, "Jaws")
		self.assertEqual(m.author, "Steven Spielberg")
		self.assertEqual(m.release_year, "1975")
		self.assertEqual(m.url, "https://itunes.apple.com/us/movie/jaws/id526768967?uo=4")
		self.assertEqual(m.rating, "PG")
		self.assertEqual(m.movie_length, 7451455)
		self.assertEqual(m.info(), "Jaws by Steven Spielberg (1975) [PG]")
		self.assertEqual(m.length(), 124)

unittest.main()
