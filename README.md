# Real Time Face detection
Face Recognition is becoming a new trend in the security authentication systems. Modern FR systems can even detect, if the person is real(live) or not while doing face recognition, preventing the systems being hacked by showing the picture of a real person. I am sure, everyone wondered when Facebook implemented the auto-tagging technique. It identifies the person and tag him/her when ever you upload a picture.

**What is Face detection?**
Face detection is a computer technology being used in a variety of applications that identifies human faces in digital images. Face detection also refers to the psychological process by which humans locate and attend to faces in a visual scene.

## Using Haar-Cascade
The Haar Classifier is a machine learning based approach, an algorithm created by Paul Viola and Michael Jones; which are trained from many many positive images (with faces) and negatives images (without faces).

_It starts by extracting Haar features from each image as shown below:_

<img src="/Images/haarfeatures.png">

## Opencv on Python

 **DEPENDENCIES**

Let's first install the required dependencies to run this code.

    OpenCV 3.2.0 should be installed.
    Python v3.5 should be installed.
    (Optional) Matplotlib 2.0 should be installed if you want to see results in an organized manner.

Note: If you don't want to install matplotlib, then replace matplotlib code with OpenCV code as shown below:

Instead of:
plt.imshow(gray_img, cmap='gray')

	
plt.imshow(gray_img, cmap='gray')

You can use:
* **cv2.imshow(window_name, image):**
This is a cv2 function used to display the image. It also takes two arguments: the first one is the name of the window that will pop-up to show the picture and the second one is the image you want to display.

* **cv2.waitKey():**
This is a keyboard binding function, which takes one argument: (x) time in milliseconds. The function delays for (x) milliseconds any keyboard event. If (0) is pressed, it waits indefinitely for a keystroke, if any other key is pressed the program continues.

* **cv2.destroyAllWindows():**
This simply destroys all the windows we created using cv2.imshow(window_name, image)



 
Text attributes _italic_, 
**bold**, `monospace`.

Horizontal rule:

---

Bullet list:

  * apples
  * oranges
  * pears

Numbered list:

  1. wash
  2. rinse
  3. repeat

A [link](http://example.com).

![Image](Image_icon.png)

> Markdown uses email-style > characters for blockquoting.

Inline <abbr title="Hypertext Markup Language">HTML</abbr> is supported.
