class Get_parametr:
  @staticmethod
  def get_paramtr(parameters_dict, method_key):
    for parameter_value in parameters_dict[method_key]:
      yield parameter_value
      