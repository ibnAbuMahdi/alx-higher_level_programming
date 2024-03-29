#!/usr/bin/python3
""" base.py """
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """ returns JSON string representation of list_dicts """
        out = "[]"
        if list_dicts is not None and isinstance(list_dicts, list)\
                and len(list_dicts) > 0:
            real_list = []
            for item in list_dicts:
                if isinstance(item, dict):
                    real_list.append(item)
            out = json.dumps(real_list)
        return out

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json version of list_objs to file """
        fname = ""
        list_dics = []
        if list_objs is not None and isinstance(list_objs, list)\
                and len(list_objs) > 0:
            for obj in list_objs:
                if isinstance(obj, cls):
                    fname = type(obj).__name__ + ".json"
                    break
            for obj in list_objs:
                if issubclass(type(obj), cls):
                    list_dics.append(obj.to_dictionary())
        else:
            fname = "Rectangle.json"

        with open(fname, "w", encoding="utf-8") as f:
            content = cls.to_json_string(list_dics)
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """ returns list version of json_string """
        out = []
        if json_string is not None and len(json_string) > 0:
            tmp = json.loads(json_string)
            for item in tmp:
                if isinstance(item, dict):
                    out.append(item)

        return out

    @classmethod
    def create(cls, **dct):
        """ create a new instance of cls """
        upd_attr = getattr(cls, "update", None)
        if callable(upd_attr):
            if dct is not None and "size" in dct:
                dum = cls(3)
                dum.update(**dct)
                return dum
            elif dct is not None and "width" in dct and "height" in dct:
                dum = cls(6, 4)
                dum.update(**dct)
                return dum

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            obj_list = []
            fname = cls.__name__ + ".json"
            with open(fname, encoding="utf-8") as f:
                string = f.read()
                json_l = cls.from_json_string(string)
                for dct in json_l:
                    obj = cls.create(**dct)
                    obj_list.append(obj)
            return obj_list
        except FileNotFoundError:
            return []

    @classmethod
    def listdict(cls, listdics):
        """ converts dictionaries to lists """
        out = []
        if "size" in listdics[0]:
            for dic in listdics:
                temp = []
                temp.append(dic['id'])
                temp.append(dic['size'])
                temp.append(dic['x'])
                temp.append(dic['y'])
                out.append(temp)
        elif "height" in listdics[0]:
            for dic in listdics:
                temp = []
                temp.append(dic['id'])
                temp.append(dic['width'])
                temp.append(dic['height'])
                temp.append(dic['x'])
                temp.append(dic['y'])
                out.append(temp)
        return out

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saves json version of list_objs to file """
        fname = ""
        dict_to_list = []
        list_dics = []
        if list_objs is not None and isinstance(list_objs, list)\
                and len(list_objs) > 0:
            for obj in list_objs:
                if isinstance(obj, cls):
                    fname = type(obj).__name__ + ".csv"
                    break
            for obj in list_objs:
                if issubclass(type(obj), cls):
                    list_dics.append(obj.to_dictionary())
            dict_to_list = cls.listdict(list_dics)
        else:
            fname = "Rectangle.json"

        with open(fname, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in dict_to_list:
                writer.writerow(row)

    @classmethod
    def list_to_dic(cls, line):
        """ converts obj list repr to dict """
        if len(line) == 4:
            temp = {}
            temp.update({"id": int(line[0])})
            temp.update({"size": int(line[1])})
            temp.update({"x": int(line[2])})
            temp.update({"y": int(line[3])})
            return temp
        elif len(line) == 5:
            temp = {}
            temp.update({"id": int(line[0])})
            temp.update({"width": int(line[1])})
            temp.update({"height": int(line[2])})
            temp.update({"x": int(line[3])})
            temp.update({"y": int(line[4])})
            return temp

    @classmethod
    def load_from_file_csv(cls):
        """ returns a list of instances """
        try:
            obj_list = []
            fname = cls.__name__ + ".csv"
            with open(fname, encoding="utf-8") as f:
                csvreader = csv.reader(f)
                for line in csvreader:
                    obj = cls.create(**(cls.list_to_dic(line)))
                    obj_list.append(obj)
            return obj_list
        except FileNotFoundError:
            return []
