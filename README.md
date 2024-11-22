# EEC174 AY Project A2: Image Mask Manipulations and Path Tracking
# Instructions (Do not clone this repo!)

Due Date: December 6, 2024 12:59PM

In this project, there are two seperate phases. In Phase 1, you will use semantic segmentation for inference and manipulate images using the output masks. In the second, Path Tracking assignment you will implement a naive version of a tracker (similar to SORT) for assigning IDs and tracking path of objects in a video. 

## Environment Setup

You are not required to use the server or docker for this lab. 

***Phase 1:*** You can use Google Colab, GPU is not necessary!!

***Phase 2:*** Same as A1. Feel free to use same environment.

## Phase 1: Image Mask Manipulation with Semantic Segmentation 

Related file: ```A2_Phase1.ipynb```

All instructions are provided in the notebook itself. There are three main sections:
- Inpaint
- Stylization
- Replacement

### Phase 1: Bonus Question

Under development!!

## Phase 2: Path Tracking

Related files: ```tracker.py```, ```yolo_path_tracker.py```

This assignment is very closely related to Mini-Project A1, where instead of using SORT, you will develop your own basic tracker.
You are provided some skeleton code to read videos in ```yolo_path_tracker.py```. Please follow a similar structure in A1, where you must:

- Convert frame to blob
- Use YOLO net to detect objects
- Apply Non-Maximum Suppression (NMS) to filter out overlapping boxes
- Update the tracker with the centroids of detected objects
- Draw bounding boxes, trails, and labels on the frame

### Tracker
Up till tracker, your code can be identical to A1. In this assignment instead of suing sort.py, we will make out own tracker ```Tracker()``` class in ```tracker.py```.

You are provided with the class and method stubs and what each method should do. There is a breakdown of ```Tracker()```:

```Tracker()```
- Initialization (__init__):
    - Initialize variables to store object IDs, their centroids, lost count, and paths.
- Registering Objects (register):
    - Assign a unique ID to the new object.
    - Store its centroid and initialize its path and lost count.
- Deregistering Objects (deregister):
    - Remove an object's data from the tracker.
- Updating Objects (update):
    - For each new set of centroids (representing objects in the current frame):
        - If there are no tracked objects, register all new centroids.
        - If there are existing tracked objects, match new centroids to existing objects based on proximity.
        - Register any new objects that don't match existing ones.
        - Update the paths and lost count for each tracked object.
        - Deregister objects that have been lost for more than maxLost frames.
- Calculating Distance (_distance):
    - Implement the method to calculate the Euclidean distance between each pair of centroids from two lists.

We will match detected objects by their closest distance to last known. You can set a maximum distance radius to look for the object, otherwise deregister the object. 
The TA has set this to ```MAX_DISTANCE = 50```. So any distances beyond that will not be counted as same ID.

### Visualization

Please store the paths in tracker for IDs. You must visualize the paths by tracking the centroids of people detected. Implement a function that does this. Make sure to remove them beyond a certain length that you find is visually suitable. You can use ```cv.line()``` to plot the path. The path should be a list of centroids returned/stored in Tracker object.

Here is the TA's sample output video (or see kartik_sample/output.mp4:

![kartik_sample/kartik_out.gif](kartik_sample/kartik_out.gif)

## Evaluation

### Grade Breakdown

- Phase 1: 60%
- Phase 2: 40%

You are allowed to work in pairs for this assignment. Please avoid excessive collaboratation with other groups.

***Note:*** There *may* be a bonus question in Phase 1 worth 10%!! However, total is still out of 100, it can cover for lost points elsewhere :) 

## Submission

Graded files

Phase 1:
- ```A2_Phase1.ipynb```

Phase 2:
- ```tracker.py```
- ```yolo_path_tracker.py```

## Credits

Kartik Patwari, Yui Ishihara, Jeff Lai, and Chen-Nee Chuah
