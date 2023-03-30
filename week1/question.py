#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 17:40:32 2023

@author: nouman
"""
import os
import importlib.util
day3_t1='day3_t1'

dir_path = os.path.dirname('/home/nouman/Downloads/training_batch/day3_t1/')

for file_name in os.listdir(dir_path):
    if file_name.endswith(".py"):
        module_name = file_name[:-3]

        module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(dir_path, file_name))
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        try:
            print(f"Email in {module_name}: {module.email}")
            result = module.solution(5)
            print(f"Solution in {module_name}: {result}")
        except AttributeError:
            print(f"AttributeError in {module_name}:")
        except (NameError) as e:
            print(f"Exception {module_name}: {e}")
       