
Anim8 is an open-source library filled with premade cross-browser CSS animations ready to take your project to the next level. Anim8 allows users to import or download web animations for faster development in normal language.

THE OUTLINE
- Introduction
- Why anim8
- Before you continue:
    - How this documentation is arranged 
    - Anim8 case
- Tutorials
    - Installation and getting started 
    - Usage:
        - In class lists
        - With JS-adding to class list
    - Utility functions 
- How to guide's
    - Changing defaults 
- Technical reference
    - Our complete list of animation classes
- How it all works
- Important to note 
- Best Practices















# INTRODUCTION
	
## WHY  “Anim8”
With anim8 you simply have the best at your fingertips with just a few words added to your class list - perfect for beginners, and those who simply want to do simple animations at break record timings. To name a few more:
Anim8 can be used as a cross-browser animation library in your online projects. Excellent for leading hints, home pages, sliders, and emphasis. They are compact files that function on desktops and can be resized without losing quality.
One of the many methods to utilize Anim8 is to copy and paste the effect into your own CSS or to reference the stylesheet. Then, simply add the effect's class name to the element you want it to be applied to.
It has a very modest file size.
Use your favourite tools without jumping through endless hoops to ensure compatibility. Anim8 "just works". We worry about compatibility so that you don’t need to. Another headache is solved. 
Exposes animation elements and parameters to use as targeting elements to add interactivity and manipulate at run-time.
Read on to find out more.


# THE ANIM8 CASE
Since our purpose is to better the developer's life we have considered a case, how do we know which class belongs to which library (eg. bootstrap) assuming you want to use some other library so we use a special case  _className .

Now to the meat…

# TUTORIALS 

## INSTALLATION AND GETTING STARTED 
To access the library, please sign in but if this is your first time using the library or don’t have an account then go ahead and create a new account by signing up
To install, go to our website and click on download and then put it in your project folder. Then how do you link it?

## IN THE HTML
```html
<link rel="stylesheet" href="<pathToWhereYouStoredIt>/anim8.css" />
```

### OR IN THE CSS

Using a string:
``` css
@import "lib/index.css";
```


Or a URL:
``` css
@import URL("lib/index.css");
```


You could also install using npm
### Install with npm:

``` 
$ npm install zuri-anim8
```
 
THEN
Import it in your CSS file:
```css
import 'zuri-anim8/lib/index.css';
```

OR

Link it in your HTML:
Include the file anim8.css 
``` html
<link rel="stylesheet" href="<pathToWhereYouStoredIt>/zuri-anim8/lib/index.css" />
```
						

# USAGE


There are two basic ways to use Anim8 and these are;

### …BY ADDING CLASSES TO THE HTML TAGS
```html
class = " _moveUp"
```

For a list of more classes do check our technical reference.

### …ADDING CLASSES WITH JAVASCRIPT
```javascript
<whatYouWantToAnim8>.classList.add("_moveUp");
```

There’s also another way of utilizing your animations;

### …USING KEYFRAMES
A keyframes animation is the default animation type and it can be used to define the behaviour of the animation from the start to the end using:
 
 ```css
 @keyframes anim8{
0%{
}
100{
}
}
```


This provides a flexible way to use Anim8.css with your current projects without having to refactor your HTML code. So at each point, you can determine what you want to happen to the animation.



## YOU WANT MORE … YOU HAVE MORE

You can also change some of the settings that come with the specific animations by using the utility functions and luckily anim8 comes with three;

### SPEED 
To change the speed of animation you can add any of this to the class list, don't forget to put your space in between!


|classes|How fast they go|
|-------|:--------------:|
|_slow  |2 seconds       |
|_slower|4 seconds       |
|_fast  |800 milliseconds|
|_faster|400 milliseconds|



### DELAY
What if you wanted to make the animation wait a bit before it starts - anim8 comes with some interesting stuff.


|classes|Delay times  |
|--------|:----------:|
|_delay-2s|2 seconds  |
|_delay-3s|3 seconds  |
|_delay-4s|4 seconds  |
|_delay-5s|5 seconds  |


### REPEAT
Or if you're feeling ‘geeky’  you can call it the iteration count. Now, what does anim8 come with?

| classes |Number of repetitions |
|---------|:--------------------:|
|_repeat-1|once                  |
|_repeat-2|twice                 |
|_repeat-3|thrice                |
|_repeat-infinite|…………Infinity   |

Now thats that but then, we know there can be no standards for these utility functions, we know your creativity is boundless, so anim8 can do more bounce to  the How To Guides for more.



## HOW TO GUIDES
### CHANGING DEFAULTS
You could simply go to the library and change stuff for example;

This is how it looks in the library…
```css
._repeat-2{
  animation-iteration-count: 2;
}
```


But then i could go and make it this and anywhere i put my _repeat-2  it will repeat 3000 times (actually for this example one could have just used  _repeat-infinite  in the class list don't you think)

```css
._repeat-2{
  animation-iteration-count: 3000;
}
```

Apart from changing the utility functions you can play around with the actual animations… 

BUT What if I make a mistake and break the library?
You can always come back and re-download. We encourage you to keep breaking it, we even added notes, and learning, at least you could tell us what you’ve done and help others grow - like the true developers we know you are.


# TECHNICAL REFERENCE
### OUR COMPLETE LIST OF ANIMATION CLASSES
You’d know what they do from their names, neat right.

### BASIC ANIMATIONS
-_moveDown
-_moveRight
-_moveLeft
-_blink
-_fade
-_bounce
-_moveUp
-_moveDown


### ATTENTION SEEKERS
-_popOut
-_tada
-_changeBgColor
-_shakeSide
-_shakeUpDown

hope to add more soon




# HOW IT ALL WORKS
We simply use the classes and add animations to these classes in the css code which makes up the library (simple CSS animations which are a lot easier than javascript animations so it's easier for you to edit). You could download the library to see the codes.

# IMPORTANT TO NOTE
You can’t use animations on inline elements, it might work on some browsers but eventually it won’t and it breaks some CSS specifications, but then there is a workaround just set the element you want to anim8’s  display: inline-block;  

# BEST PRACTICES
Animations can greatly improve an interface's UX, but it's important to follow some guidelines to not overdo it and deteriorate the user experience on your web-things. Following the following rules should provide a good start.
You should avoid animating an element just for the sake of it.
Don't animate large elements
Animating the '<html>' or '<body>' tags is possible, but you should avoid it
You should avoid endless animations. It will just distract your users and might annoy a good slice of them



