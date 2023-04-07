class Options_to_dict:
  @staticmethod
  def options_to_dict(methods_list, parameters_list):
    return {methods_list[i]: parameters_list[i] for i in range(len(methods_list))} 
    