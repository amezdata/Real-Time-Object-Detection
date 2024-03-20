# Real-Time-Object-Detection  

**Overview**  
This project involves a Python-based application using OpenCV for real-time object detection and measurement. It captures video through an external camera, processes frames to detect objects, calculates their sizes in millimeters, and visually annotates these measurements onto the video feed. This application serves as a practical tool in fields such as quality control, manufacturing, and education, where real-time measurement and detection can significantly enhance operational efficiency and learning outcomes.

**Program Description**  
This Python application uses OpenCV to achieve real-time object detection and measurement through a video stream from an external camera. It processes video frames by cropping, converting them to grayscale, and applying a binary threshold for object segmentation. The program detects objects within these frames, calculates their dimensions in millimeters, and annotates the video feed with this information, alongside the total count of detected objects. This feature set makes it particularly useful for applications requiring real-time analysis, such as quality control in manufacturing or educational demonstrations in computer vision. The application provides visual feedback by highlighting detected objects with circles and overlaying text annotations for object sizes, enabling users to assess object dimensions visually. 

**Key Functions**  
- Real-Time Video Processing: It processes video frames in real time, allowing for immediate detection and measurement of objects as they appear in the camera's view.  
- Automatic Measurement Calculation: Automatically calculates the size of detected objects, converting the area in pixels to millimeters, providing a useful metric for size analysis.  
- Visual Feedback: Offers visual feedback by annotating frames with object measurements and drawing circles around detected objects (green over 20mm and red below this mark).  
- User Interaction: Allows users to terminate the program by pressing 'q'.

**Limitations**   
- Fixed Camera Position: This script assumes a fixed camera position and does not account for dynamic changes in the camera's orientation or position.  
- Region of Interest: The frame cropping is hardcoded, which may not be suitable for all use cases. Dynamic adjustment of the region of interest would be more versatile.  
- Lighting Conditions: The application's accuracy can be affected by varying lighting conditions, which might necessitate additional lighting control mechanisms for consistent performance or threshold modification. 
- Object Complexity: Highly complex or overlapping objects might not be accurately detected or measured, limiting the application's effectiveness in crowded or complex scenes.
- Scale Conversion: The diameter calculation relies on a specific conversion scale, which might not be accurate for all object sizes or shapes, potentially affecting measurement precision.  
