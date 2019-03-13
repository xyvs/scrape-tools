#!/usr/bin/env python3

#######################################
#                                     #
#          goalkicker - V1.0          #
#                                     #
#######################################
#                                     #
# Description                         #
#                                     #
# Download books from goalkicker.com  #
#                                     #
# Usage                               #
#                                     #
# ./goalkicker_downloader.py or       #
# python3 goalkicker_downloader.py    #
#                                     #
# Changelog                           #
#                                     #
# 12/03/19 - Version 1.0              #
# 12/03/19 - File created!            #
#                                     #
#                                     #
#  Author - https://github.com/xyvs   #
#                                     #
#######################################


import requests
import re
import os

from bs4 import BeautifulSoup


def DownloadBook(url,pdf_name):
	
	# File route
	file_route = f'goalkicker.com/{pdf_name}'
	
	# Check if file exists
	file_exists = os.path.isfile(file_route)

	if not file_exists:

		# Get book content
		response = requests.get(url)

		# Write book into the system
		with open(file_route, 'wb') as file:  
			file.write(response.content)

		print(f'[New!]')

	else:   
		print(f'[Done]')


def main():

	# Base URL
	base_url = 'https://goalkicker.com/'

	# Get page
	response = requests.get(base_url)
	soup = BeautifulSoup(response.text, 'html.parser')

	# Get all book
	books = soup.findAll("div", {"class": "bookContainer"})

	# Downloading book output
	print(f'[Total] {len(books)} books to download.')

	# Define download directory
	DIRECTORY_PATH = 'goalkicker.com'

	# Check if directory exists
	folder_exists = os.path.isdir(DIRECTORY_PATH)

	# Make new folder
	if not folder_exists:
		
		print(f'[Directory] Directory {DIRECTORY_PATH} created!')

		os.mkdir(DIRECTORY_PATH)

	else:
		print(f'[Directory] Directory {DIRECTORY_PATH} already exists!')

	# Iterate books
	for book in books:
		
		# Get book url
		book_url = re.sub('/','',book.a['href'])

		# Get pdf url
		pdf_url= re.sub(r'Book.*', 'NotesForProfessionals.pdf', book_url)

		# Get full url
		full_url = f'{base_url}{book_url}/{pdf_url}'

		print(f'[Book] Downloading {book_url}', end =" ")

		# Download books
		DownloadBook(full_url,pdf_url)

	print('[Finish] All done!')


if __name__ == '__main__':
	main()