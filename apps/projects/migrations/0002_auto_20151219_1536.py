# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 15:36
from __future__ import unicode_literals
from django.db import migrations
from datetime import datetime


def import_projects(apps, schema_editor):
    """
    Load up initial applications
    :param apps:
    :param schema_editor:
    :return:
    """
    Project = apps.get_model("projects", "Project")
    data = [
        ("Appetite", "appetite.png", datetime(2015, 2, 7)),
        ("Portfolio", "portfolio.png", datetime(2015, 12, 19),
        ("Sage", "sage.png", datetime(2015, 11, 26)),
        ("Gitit-Notes", "gitit-notes.png", datetime(2015, 5, 29)),
        ("Mini-Java", "mini-java.png", datetime(2014, 2, 15)),
        ("Pong", "pong.png", datetime(2015, 10, 1)),
        ("Project Euler", "project-euler.png", datetime(2015, 4, 1))),
        ("Infection", "infection.png", datetime(2015, 2, 14)),
        ("Huffman Encoding", "huffman-encoding.png", datetime(2014, 4, 26)),
        ("Fifth CAM", "fifth.png", datetime(2015, 5, 30)),
        ("Lodestar", "lodestar.png", datetime(2013, 6, 20)),
        ("Mingle", "mingle.png", datetime(2014, 7, 18)),
    ]
    descriptions = [
        """
        An Android/iOS application designed to work in a manner similar to Songza. That is, based on a perceived mood provided by the user, Appetite queries up local venues that align with the user's feelings. The application was written as a submission to the Carolina Creates Entrepreneurial competition where Appetite placed 8th.
        """,
        """
        Refers to this website- my online portfolio and blog. It is written using Python (with the Django 1.9 backend).
        """,
        """
        A C++ PEG packrat parser written experimentally for a more thorough understanding of topdown parsing. This includes a library of regular expressions and scanning utilities.
        """,
        """
        Consists of various notes and resources I've collected regarding a variety of different mathematical concepts (e.g. Abstract Algebra, Differential Equations, Linear Algebra, etc.). It is written underneath using custom Haskell plugins and the gitit library, which in turn runs on Happstack.
        """,
        """
        A custom compiler, written in Java, for a subset of the Java language. The compiled code is written for a custom machine called mJAM (which itself is compiled to Java bytecode).
        """,
        """
        A custom version of the classic arcade game Pong in System Verilog and built onto the Artix FPGA. This works via a custom ALU intended to process an arbitrary MIPS program with a modified memory configuration allowing direct memory access between the board, the keyboard, and a monitor via the VGA specification.
        """,
        """
        A solution set, written in Haskell, for problems on the site Project Euler. In the process of solving problems, I maintain a core set of functionality in the "Euler" module.
        """,
        """
        A Khan Academy project written in C++ (with visual components relying on the SFML library) designed to simulate the needs for teacher/students pairs to be able to work on the same type of software regardless of who is teaching who. That is, a teacher can teach a student who in turn could also potentially teach someone else, or the original teacher.
        """,
        """
        A graphical implementation written in Java of the huffman encoding compression algorithm. The program appears to work with the various files tested, though this testing was not rigorously performed. It enables selection of files to compress; it will also display the compression table and decompression table during compression and decompression of files respectively.
        """,
        """
        A Cellular Automata Machine (CAM) library written in Python (and using the Numpy library underneath) loosely based off the CAM Forth language as described in "Cellular Automata Machines" by Toffoli and Margolus. It incorporates N-Dimensional Cellular Automata, an arbitrary count of bit planes and description of neighborhoods, and timing specifications for granular viewing.
        """,
        """
        An iOS application intended to allow users to generate events and create groups with random people so no one has to go anywhere alone. It allows user's to create groups of arbitrary size, create events to be viewed in a swiping manner (e.g. Tinder), and collaborate with group members via integrated group chats, or the sharing of user information (which can be privatized).
        """,
    ]
    for i in range(len(data)):
        Project(title=data[i][0], img_src=data[i][1], description=descriptions[i], date=data[i][2]).save()


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_projects),
    ]
