# Jus Mundi Coding Task

Author: Rafael Magalhaes

Date: 13/07/2024 (dd/mm/yyyy)

## 1 - The Problem

To solve a Code Kata that challenge on creating a 'number value' to 'number name' converter, specific to French language.
The objective is to use it as an artifact to base a discussion on programming techniques.

**INPUT**: list of numbers (numerical)

**OUTPUT**: list of French numbers (words)

**Dataset input example**:

 [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175, 199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000, 11111, 12345, 123456, 654321, 999999]

## 2 - Code usage

### 2.1 Importing as function

From any python script import the function from module `numbers_converter.py` as:

```python
from numbers_converter import numbers_converter

example_list = [1, 10, 1111, 34567, 999999]
numbers_name = numbers_converter(example_list)
print(numbers_name)
```

### 2.2. Standalone code

Within the module directory execute the `numbers_converter.py` script to iterative usage:

```bash
$ python numbers_converter.py
"Enter a number between 0 and 999999 to get it written, or <enter> to random trial:" 245
"deux-cent-quarante-cinq"
```

without input number the program will generate five random numbers list from 1 to 999999 range.

```bash
$ python numbers_converter.py
"Enter a number between 0 and 999999 to get it written, or <enter> to random trial:"
[(292522, 'deux-cent-quatre-vingt-douze-mille-cinq-cent-vingt-deux'),
 (181499, 'cent-quatre-vingt-un-mille-quatre-cent-quatre-vingt-dix-neuf'),
 (62632, 'soixante-deux-mille-six-cent-trente-deux'),
 (541358, 'cinq-cent-quarante-et-un-mille-trois-cent-cinquante-huit'),
 (68591, 'soixante-huit-mille-cinq-cent-quatre-vingt-onze'),
 (239376, 'deux-cent-trente-neuf-mille-trois-cent-soixante-seize'),
 (470702, 'quatre-cent-soixante-dix-mille-sept-cent-deux'),
 (454335, 'quatre-cent-cinquante-quatre-mille-trois-cent-trente-cinq'),
 (117766, 'cent-dix-sept-mille-sept-cent-soixante-six'),
 (307125, 'trois-cent-sept-mille-cent-vingt-cinq')]
```

### 2.3. Using the test script 

If you want just to check the given input from Jus Mundi instruction, use the `test_numbers_converter.py` directly from terminal:

```bash
$ python test_numbers_converter.py
[(0, 'zéro'),
 (1, 'un'),
 (5, 'cinq'),
 (10, 'dix'),
 (11, 'onze'),
 ...
 (11111, 'onze-mille-cent-onze'),
 (12345, 'douze-mille-trois-cent-quarante-cinq'),
 (123456, 'cent-vingt-trois-mille-quatre-cent-cinquante-six'),
 (654321, 'six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un'),
 (999999, 'neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf')]
```

## 3 - Constraints and important considerations

The instructions shared by email states the following (quote):

"Normally, a basic/rushed implementation takes less than 20ish minutes.
Do not spend more than two hours on the kata to code something you are proud of.
If you use some LLM tool such as GitHub Copilot, or ChatGPT, please note it in the readme.md with the prompts used."

From this I did interpret as:

- It is important to make it fast, surelly correct, but not perfect nor well polished as it was the final code in production.
- Because it needs to be done fast, one main case need to be implemented, other French variations would be coded later (Belgic, Canada, Afrique, Suisse, etc).
- I did not use any LLM or any other autocomplete coding support tool during all coding nor documentation work.

## 4 - Author considerations

Because French isn't my native language it demands me an effort to understand the language specificities. To do that I really get deep on Algorithm instructions (Jus Mundi Kata) and the given reference (Wikipedia Article on French Numbers). The main concern wasn't about the 60, 70, 80, 90 number constructions but, the rules about '-et', '-et-un', 'plurals', the numbers under 20, and all the Country specific variations.

I did the following main steps during the construction of the solution and making it accessible by Jus Mundi:

### First moment: problem understading (around 17 minutes)

- Read all given text from Jus Mundi and Wikipedia and take notes
- Understanding of the problem and specially understading the french specific terminology to number names
- No coding during this time
- No modeling during this time

### Second moment: effectively modeling and coding (29 minutes)

- Some time to draw something on paper (it helps me on modeling the problem)
- modeling the problem in sub-chunks (unites, dizaine, centaine, mille) to compose the final solution based on small solutions (divide and conquer)
- to separate the solution (converter) from the specific input from the required list, because it is only one way to use the solution.
- I chose recurrency because it is a good way to solve the problem and to make it extensible to millions, billions, etc. Each sequence of three numbers on any magnitude (hundreds, thousands, millions, etc.) repeats itself in someway with small specificities.
- I did choose to dealing with the input data type and also on processing type as problem based rule (with 'cases'), so it would be better to read, to improve and to reduce the complexity to maintain.
- I did not choose going on number calculations, algebrical functions and its result to later do comparison approach because it reduce the readbility in initial modeling and demands more effort on every improvement and extension of code until it get the final solution. Of course, if efficiency, performance or hardware/software architectural constraints demanded, it could be changed.
- I did choose to go on content (most string) chompharison approach because it is simple to read, to increment and to find where to change on improvments or extensions.
- I rapidly tested the code output but only with two approaches: 1 - the informed input list, 2 - random chunk of 5 numbers, for some rounds.

### Third step: document the code, create the Readme [this text], and submit code on github (around 48 minutes)

- I spent more time on document the description, the used reasoning, concerns, found inconsistencies and choices.
- Doing that I believe it gives more content to talk about, to better remember my descisions and to better explain my specific approach and difficulties on solve the challenge.

## 5 - Inconsistencies between Jus Mundi instructions and the reference given (Wikipedia)

I found one important small divergence about the plurals constructions on "milles" on given instructions. The Code Kata instructions and Wikipedia reference article disagree on this subject.

### 5.1. Reference Wikipedia instruction

The principal reference given is an article from [Wikipedia](https://fr.wikipedia.org/wiki/Nombres_en_français)

Artifacts:

#### In the initial table it is possible to read

- `10 000` - dix mille (without s)
- `100 000` - cent mille (without s)

#### In section 'Accords'
  
There are instructions only related to '80', 'cent', and 'cents' (plural) but not related to 1000 variations on mille

#### In section 'Adjectif cardinaux'

- `80 000` - quatre-vingt mille (orthographe traditionnelle) ou quatre-vingt-mille (orthographe de 1990)

Both 'traditionnelle' and 'accord 1990' the plural of mille still mille (without s).

- `300 000` - trois cent mille (orthographe traditionnelle) ou trois-cent-mille (orthographe de 1990)

Even 'cent' plural rule isn't used when it comes to thousands position, neither mille go with 's'.

### 5.2. Instructions given by Jusmundi

The instruction on [Kata site](https://jusmundi.notion.site/Kata-number-to-french-converter-58d8855436f84afe97e98b7aa364fd), states on section named '**100 and more**', specifically on '**plurals of "cent" et "mille"**' that it is imperative to use 's' on 'cent' and 'mille' if it ends the words and exemplify with:

- `3 000` = `3 * 1000` = "trois-milles"
- `200000` = `2 * 100 * 1000` = "deux-cent-milles", without S at "cents", but with S at "milles"
- `180000` = `(100 + 4 * 20) * 1000` = "cent-quatre-vingt-milles", without S at "vingt", but with S at "milles"

### 5.3. Decision on coding as consequence of this

- **I did CHOOSE TO FOLLOW Jus Mundi Instruction (the client instructions)**
- **I DID NOT choose to follow Wikipedia instructions**

## 6 - Possible improvements

Taking in mind that time was the main driver and recommended concern, it was quite impossible to consider other usual programming considerations without code reusing, templates, boilerplates or coding support tools like: autocomplete, Copilot, etc.

I list some of possible continuity improvements, as follow:

- Extend to adapt to Belge, Suisse et Congo, and other variations to widle support French language
- Documentation and usage examples with tools like mkdocs or sphinx
- Using typing hints to reduce type errors with checkage before code running
- Test suit for general numbers and specific heuristic well known for this task
- Package the code with pip or pipx to use the Pyhton language repo or to better distribute on company repos
- Disponibility through web API (FastAPI, Flask, etc..) to make it accessible as a service
- Create docker images to make deployable by company structure

Thank you.
