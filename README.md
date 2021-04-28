# bannerMaker
Create tidy text based banners for CLI based systems, servers and appliances.

**Author:** Brett Verney</br>
**Version:** v0.1 | 28-04-2021

As a Network Engineer I feel I have wasted far too many hours trying to centre text while creating Message of the Day and Authentication Failure banners for CLI based network infrastructure i.e. Cisco and Aruba.

This tool takes away that pain.

Really though, it takes one or more paragraphs of text and centres it between a box depicted by asterisks. Nothing more, nothing less.

It also preserves blank lines which other tools don't without great difficulty.

## Requirements

- Python 3+
- Python Libraries
  - parawrap

## Basic Script Usage

```python bannerMaker.py <input_file>```<br><br> 
Where **<input_file>** is a text file containing one or more paragraphs of text.

The resulting banner will be output to **banner.txt**

## Example

A file named **input.txt** contains the following text:<br>

![bannerMaker input example1](https://github.com/wifiwizardofoz/bannerMaker/blob/main/input_example1.png)<br>

Executing the script and specifying the **input.txt** file as an argument:

```python bannerMaker.py input.txt```

Creates a file named **banner.txt** containing the following:<br>

![bannerMaker output example1](https://github.com/wifiwizardofoz/bannerMaker/blob/main/output_example1.png)

Another example:<br>

![bannerMaker output example2](https://github.com/wifiwizardofoz/bannerMaker/blob/main/output_example2.png)

The whitespace is preserved by utilising 'space' characters instead of tabs so that the output can copied and pasted directly to the CLI or config file as is.

## Customisation

The script uses box width and text padding values that are considered safe for most terminal CLI appliances by default. These can be modified within the script itself. It is best to use even integers:
```
box_width = int(76)
padding = int(4)
```
You can also modify the heeading at the top of the banner:
```
heading = ('WARNING')
```
