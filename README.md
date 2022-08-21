**Detection of helmet-less riders in Indian roads using Machine
learning**

**Context:**

Indian traffic system is one of the busiest in the world. Naturally, it
is hard to manually monitor and enforce traffic laws everywhere. So, we
propose a novel solution for the enforcement of traffic laws on Indian
roads using Artificial Intelligence and computer vision.

**Problem statement:**

According to Ministry of Road Transport and Highways, as many as 158,964
two-wheeler road accidents took place in India in 2020, which caused
56,873 deaths, a fraction of which occurred due to the absence of a
helmet. In spite of various campaigns launched by various state
government and introduction of various penalties, this is still a
problem in Indian roads and endangers India's young citizens' life.

**Our solution:**

We propose an automated system to enforce the use of helmet in Indian
roads and the penalty collection system.

**Proposed Methodology:**

![](./media/media/image1.png){width="5.641666666666667in"
height="2.4583333333333335in"}

**Development Process:**

1.  Data collection & labelling: We used YOLOv5, which is an open-source
    deep learning platform for the detection of motorcycle, helmet and
    helmetless riders and their number plate. The data necessary for the
    training of the model was collected from our college campus, and
    labelled manually using MakeSense, which is an online annotation
    tool.

2.  Training: YOLOv5 is fed the labelled images, and it learns to
    predict the co-ordinates of the bounding boxes.

Example detection output:

![](./media/media/image2.jpeg){width="3.7416666666666667in"
height="3.7954068241469816in"}

![](./media/media/image3.jpeg){width="2.370291994750656in"
height="1.3583333333333334in"}![](./media/media/image4.jpeg){width="1.4583333333333333in"
height="1.7080063429571304in"}

After our model detects a rider without a helmet, it scans and crops the
number plate of the two-wheeler, which is then passed to an OCR package.
For our project, we used python's EasyOCR library.

OCR on number plate:

![](./media/media/image3.jpeg){width="2.908333333333333in"
height="1.6666666666666667in"}

After recognizing the license-plate number, our model queries a database
which contains the information of all of the registered riders in India
for their Name, Phone number and email. An e-challan is issued on the
rider's name, which they are notified using mail and text SMS with
proper information about where, when and what type of violation was done
by him.

Sample SMS & Mail alert:

![](./media/media/image5.jpeg){width="3.1083333333333334in"
height="2.7in"}

![](./media/media/image6.jpeg){width="3.033333333333333in"
height="2.4823687664041993in"}

We did not have access to actual Indian vehicle registration data, so we
used a dummy database, which we created and tested on. For the payment
portal, we used a RazorPay payment gateway, which will then store the
payment information in a database.

> Payment Dashboard of admin:

![](./media/media/image7.jpeg){width="4.083333333333333in"
height="3.2666666666666666in"}

**Future scope:**

Our system can be used to detect and enforce any traffic violation. The
most novel Idea would be to detect overweighing detection and dangerous
carriage of construction materials.

During the actual implementation, the system requires High-definition
CCTV cameras, and GPU accelerated servers for real time detection from
CCTV footage. The actual national vehicle-registration database should
be used, and an actual e-challan payment gateway should be connected to
the database.

-X-


### To monitor the data run:

```
cd yolo && python traffic-monitor.py --source ../data/images/train/IMG20220811133939.jpg --weights 'runs/train/exp/weights/best.pt'  --save-crop && cd .. && python ./main.py 
```
