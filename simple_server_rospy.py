#!/usr/bin/env python3

import rospy
from (srvPackageName).srv import (srvFileName), (srvFileName)Response

def server_callback(req):
    rospy.loginfo("Received request: %s", req.words.data)

    words = req.words.data.split(" ")
    resp = (srvFileName)Response()

    if req.count_articles.data:
        english_articles = ["a", "an", "the"]
        resp.num_articles.data = len([word for word in words
                                      if word in english_articles])
    
    resp.num_words.data = len(words) - resp.num_articles.data

    return resp

if __name__ == '__main__':
    rospy.init_node('rospy_simple_server_node', anonymous=False)
    rospy.Service('rospy_word_count', (srvFileName), server_callback)
    rospy.spin()