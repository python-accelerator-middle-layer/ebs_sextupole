#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <Sextupole.h>
#include <iostream>

namespace py = pybind11;

void *mag_create(std::string strength_file_name, std::string param_file_name, std::string mag_s_n) {

    std::cout << "Sextupole::init" << std::endl;
    MagnetModel::Sextupole *sextu = new MagnetModel::Sextupole();
    sextu->init(strength_file_name,param_file_name,mag_s_n);
    return sextu;

}

std::vector<double> compute_strengths(void *ptr,double magnet_rigidity_inv,std::vector<double>& in_currents) {

  MagnetModel::Sextupole *s = (MagnetModel::Sextupole *)ptr;
  std::vector<double> out_strengths;
  s->compute_strengths(magnet_rigidity_inv,in_currents,out_strengths);
  return out_strengths;

}

std::vector<double> compute_currents(void *ptr,double magnet_rigidity,std::vector<double>& in_strengths) {

  MagnetModel::Sextupole *s = (MagnetModel::Sextupole *)ptr;
  std::vector<double> out_currents;
  s->compute_currents(magnet_rigidity,in_strengths,out_currents);
  return out_currents;

}

PYBIND11_MODULE(ebs_sextupole_bind, m) {
    m.doc() = "EBS Sextupole magnet model for PyAML";
    m.def("mag_init", &mag_create,py::return_value_policy::reference);
    m.def("compute_strengths",&compute_strengths);
    m.def("compute_currents",&compute_currents);
}