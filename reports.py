#!/usr/bin/env python3

import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()

    report_title = Paragraph(title, styles["h1"])
    flow_paragraph = Paragraph(paragraph, styles["h3"])

    report.build([report_title, flow_paragraph])
