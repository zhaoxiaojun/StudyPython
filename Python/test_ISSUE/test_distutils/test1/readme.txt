基本术语：

模块（module）：
    Python中可复用的基本代码单元，可由其他代码import的一块代码，这里我们只关注三种类型的模块：纯python模块，扩展模块和包。

纯python模块（pure Python module）：
    由python编写的模块，包含在单独的py文件中（或者是pyc/pyo文件）。

扩展模块（extension module）：
    由实现Python的底层语言编写的模块（C/C++ for Python, Java for Jython）。通常包含在单独的动态加载文件中，比如Unix中的so文件，windows中的DLL文件，或者是Jython扩展的java类文件。（注意，目前为止Distutils只能处理Python的C/C++扩展）

包（package）：
    包是含其他模块的模块，经常由包含__init__.py文件的目录发布。

Root包（root package）：
    包层次关系中的根（它不是真正的包，因为它不包含__init__.py文件）
