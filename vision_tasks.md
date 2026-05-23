# Image Classification
Image Classification is the process of categorizing images into predefined classes. In machine learning, models learn to recognize and assign labels to entire images. This relies on algorithms trained on labeled datasets, learning to associate input images with categories such as "flood", "earthquake damage", or "wildfire".

## Types of Image Classification
- **Single-label classification**: Each image is assigned to one category.  
  *Example:* Classify a satellite image as showing either "flood damage" or "earthquake damage".  

- **Multi-label classification**: An image may belong to multiple categories simultaneously.  
  *Example:* A disaster image might show both "flooded roads" and "collapsed buildings", and the model assigns both labels.  

## Disaster Use Case
In disaster management, classification helps rapidly identify disaster types from satellite or aerial imagery. Deep learning models, particularly Convolutional Neural Networks (CNNs), are employed to categorize images into disaster types such as *flood*, *earthquake*, or *wildfire*. This enables faster response and resource allocation.


# Object Detection
Object Detection involves identifying and locating multiple objects within an image or video. Unlike classification, which assigns a single label to the entire image, detection provides both the category of each object and its location. Models output bounding boxes (defined by pixel coordinates) around detected objects, along with labels that describe what was found.

## Example
If a disaster image shows collapsed buildings and stranded vehicles, the model will:
- Label each object (e.g., "damaged building", "vehicle").
- Draw bounding boxes around them to indicate their positions.

## Disaster Use Case
Object detection is critical in disaster response because it helps identify:
- **Victims** in rescue imagery.
- **Damaged structures** such as collapsed bridges or houses.
- **Vehicles** that may block roads or assist evacuation.
- **Hazardous materials** that pose safety risks.

Real-time detection algorithms such as **YOLO (You Only Look Once)** are especially effective in disaster scenarios. Their speed and ability to work under low-visibility conditions (e.g., smoke, debris, poor lighting) make them valuable for rapid assessment and emergency decision-making.

# Image Segmentation
Image Segmentation is a computer vision technique that divides an image into multiple segments or regions, making it easier to analyze and understand specific parts of the image. Unlike classification (which assigns one label to the whole image) or detection (which draws bounding boxes around objects), segmentation works at the **pixel level**, identifying object boundaries and relevant features with high precision.

## Example
Segmentation can separate different regions in a disaster image:
- Floodwater vs. dry land
- Collapsed structures vs. intact buildings
- Roads vs. blocked evacuation routes

## Disaster Use Case
In disaster management, segmentation is especially valuable for **damage assessment and recovery planning**. Deep learning models (such as U-Net or Mask R-CNN) are applied to satellite or drone imagery to:
- Map flooded roads and neighborhoods
- Identify collapsed structures
- Detect blocked evacuation routes
- Assess the overall extent of damage

This pixel-level analysis provides emergency responders with detailed maps, enabling more effective resource allocation and faster recovery efforts.




