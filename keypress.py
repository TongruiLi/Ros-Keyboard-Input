#!/usr/bin/env python
#import getch
import rospy
from std_msgs.msg import String #String message 
from std_msgs.msg import Int8
from pynput.keyboard import Key, Listener


################################
# created by yuvaram
#yuvaramsingh94@gmail.com
# modified by Tongrui Li
################################\
pub = rospy.Publisher('key',Int8,queue_size=10) # "key" is the publisher name
rospy.init_node('keypress',anonymous=True)
rate = rospy.Rate(20)#try removing this line ans see what happens

def on_press(key):

    if hasattr(key, "char") and key.char == "w":
        print("Entering on press event for w")
        rospy.loginfo(str(1))# to print on  terminal 
        pub.publish(1)#to publish
    print('{} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

