class Class_iterator:
  @staticmethod
  def class_iterator(fn_get_paramtr, params, module):
    for method_name in params:
      getattr(module, method_name)(*fn_get_paramtr(params, method_name)) 
  