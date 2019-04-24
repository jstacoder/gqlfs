import graphene
from pathlib2 import Path


class BaseFileSystemEntry(object):
    name = graphene.String()


class BaseFileSystemItem(object):
    path = graphene.String()


class BaseFileSystemChild(object):
    parent = graphene.Field(lambda: Directory)


class FileSystemChildInput(object):
    parent = graphene.InputField(lambda: DirectoryInputType)


class FileSystemItem(BaseFileSystemEntry, BaseFileSystemItem, BaseFileSystemChild):
    pass


class FileSystemContent(object):
    content = graphene.String()


class File(FileSystemItem, FileSystemContent, graphene.ObjectType):


    def resolve_content(self, info):
        with Path(self.path) as f:
            return f.read_text()


class FileInput(BaseFileSystemEntry, FileSystemChildInput, FileSystemContent, graphene.InputObjectType):
    pass


class DirectoryBaseType(FileSystemItem):
    pass


class DirectoryInputType(BaseFileSystemItem, graphene.InputObjectType):
    parent = graphene.InputField(lambda: DirectoryInputType)


class Directory(DirectoryBaseType, FileSystemChildInput, graphene.ObjectType):
    children = graphene.List(lambda: FileSystemEntry)


class FileSystemEntry(graphene.Union):
    class Meta:
        types = (Directory, File)


class HelloType(graphene.ObjectType):
    message = graphene.String()

    def resolve_message(self, info):
        return "hello {message}".format(
            message=self.message
        )