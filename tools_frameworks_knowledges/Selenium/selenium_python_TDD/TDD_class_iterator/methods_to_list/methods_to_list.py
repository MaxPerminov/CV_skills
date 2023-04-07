class Method_to_list:
  @staticmethod
  def methods_to_list(module):
    return [method for method in dir(module) if method.startswith('__') is False]
    