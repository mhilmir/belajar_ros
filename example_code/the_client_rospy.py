#!/usr/bin/env python3

import rospy
from (srvPackageName).srv import (srvFileName), (srvFileName)Request

if __name__ == "__main__":
    rospy.init_node("rospy_simple_client_node", anonymous=False)
    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        rospy.wait_for_service("rospy_word_count")
        try:
            word_count = rospy.ServiceProxy("rospy_word_count", (srvFileName))

            req = (srvFileName)Request()
            req.words.data = "a test from the client node for a simple server client"
            req.count_articles.data = True

            resp = word_count.call(req)

            rospy.loginfo("Result -> Num of words: %s", resp.num_words.data)
            rospy.loginfo("Result -> Num of articles: %s", resp.num_articles.data)

        except rospy.ServiceException as e:
            rospy.loginfo("Service call failed: %s", e)
        
        rate.sleep()