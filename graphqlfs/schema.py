import os
from pathlib2 import Path
import graphene

from .types import (
    HelloType,
    File,
    Directory, 
    DirectoryInputType,
    FileInput,
)

class Query(graphene.ObjectType):
    hello = graphene.Field(HelloType, msg=graphene.String(required=True))

    get_directory = graphene.Field(Directory, directory_input=graphene.Argument(DirectoryInputType))
    get_file = graphene.Field(File, file_input=graphene.Argument(FileInput))

    def resolve_get_directory(self, info, directory_input=None):
        print(directory_input.path)

        dir_path = Path(directory_input.path)
        children = []
        for itm in dir_path.iterdir():
            if itm.is_file():
                if '~' not in itm.name and not itm.name.startswith('.'):
                    children.append(File(name=itm.name, path=str(itm.absolute())))
            elif itm.is_dir():
                children.append(Directory(
                    name=itm.name,
                    path=str(itm.absolute()),
                ))
        return Directory(
            name=dir_path.name,
            path=str(dir_path.absolute()),
            children=children,
        )

    def resolve_hello(self, info, msg=None):
        return HelloType(message=msg)
        

schema = graphene.Schema(query=Query)


def recursive_path_objs(path, parent=None):
    if '.pyc' in path.name or '.lock' in path.name or '~' in path.name or path.name.startswith('__'):
        return None
    if path.is_file():
        return File(
            name=path.name,
            path=str(path.absolute()),
            parent=parent,
        )
    rtn = {
        'name': path.name,
        'path': str(path.absolute(

        )),
        'children': [],
        'parent': parent,
    }
    if path.is_dir():
        for d in path.iterdir():
            if (('.pyc' not in path.name) and ('.lock' not in path.name) and (not path.name.endswith('~'))):
                print(d.name)
                rtn['children'].append(recursive_path_objs(d, path))
    rtn['children'] = [_ for _ in rtn['children'] if _ is not None]
    return Directory(**rtn)

    
