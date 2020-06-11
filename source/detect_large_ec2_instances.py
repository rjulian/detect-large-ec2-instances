""" Module for DetectLargeEc2Instances """

import json
import os

import boto3
from reflex_core import AWSRule


class DetectLargeEc2Instances(AWSRule):
    """ Detects EC2 Instances that are not a certain type. """

    def __init__(self, event):
        super().__init__(event)

    def extract_event_data(self, event):
        """ Extract required event data """
        self.instance_type = event["detail"]["requestParameters"]["instanceType"]

    def resource_compliant(self):
        """
        Determine if the resource is compliant with your rule.

        Return True if it is compliant, and False if it is not.
        """
        return self.instance_type == "t2.micro"

    def get_remediation_message(self):
        """ Returns a message about the remediation action that occurred """
        return f"An instance was launched with disallowed type: {self.instance_type}."


def lambda_handler(event, _):
    """ Handles the incoming event """
    rule = DetectLargeEc2Instances(json.loads(event["Records"][0]["body"]))
    rule.run_compliance_rule()
