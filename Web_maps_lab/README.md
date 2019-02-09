# Filming locations
Python modules used to build a map which represents places
of filming films from IMDB database, represented by locations.list

## Usage
Run module ```Map_final.py``` and chose year and maximum ammount of 
locations to be displayed on the map. It will be saved in ```Films_map.html```
To view it simply open created ```html``` file.

## What can be seen
All locations are divided into three groups: ```busy```, with the green color, 
```casual``` with orange and ```lazy``` with red.
The location is ```busy``` if there were filmed more than 10 films that year,
```casual``` - more than five, ```lazy``` - less than six.

## Known issues
Some of the locations in ```loctions.list``` does not 
satisfy ```geopy``` requirements
Depending on the ammount of places to show, and your 
network speed, it may take a long time to load.

## Meaning and usage of tags in ```html``` file
```<!DOCTYPE html>``` - is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in <br />
```<head>``` - container for metadata (data about data) and is placed between the <html> tag and the <body> tag <br />
```<meta>``` - provides metadata about the HTML document<br />
```<script>``` - s used to define a client-side script (JavaScript)<br />
```<link>``` - defines a link between a document and an external resource<br />
```<style>``` - used to add CSS style rules to an HTML document<br />
```<body>``` - defines the main content of the HTML document or the section of the HTML document that will be directly visible on web page<br />
```<div>``` - efines a division or a section in an HTML document<br />
