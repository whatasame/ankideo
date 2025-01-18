#pragma once

// @generated by torchgen/gen.py from Function.h

#include <ATen/Context.h>
#include <ATen/DeviceGuard.h>
#include <ATen/TensorUtils.h>
#include <ATen/TracerMode.h>
#include <ATen/core/Generator.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <optional>



#include <ATen/ops/mps_convolution_backward_ops.h>

namespace at {


// aten::mps_convolution_backward(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask) -> (Tensor, Tensor, Tensor)
inline ::std::tuple<at::Tensor,at::Tensor,at::Tensor> mps_convolution_backward(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  ::std::tuple<at::Tensor,at::Tensor,at::Tensor> mps_convolution_backward(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask);
  }
}

// aten::mps_convolution_backward(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask) -> (Tensor, Tensor, Tensor)
inline ::std::tuple<at::Tensor,at::Tensor,at::Tensor> mps_convolution_backward_symint(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  ::std::tuple<at::Tensor,at::Tensor,at::Tensor> mps_convolution_backward(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask);
  }
}

// aten::mps_convolution_backward.out(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2) -> (Tensor(a!), Tensor(b!), Tensor(c!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_out(at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask, out0, out1, out2);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_out(at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask, out0, out1, out2);
  }
}

// aten::mps_convolution_backward.out(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2) -> (Tensor(a!), Tensor(b!), Tensor(c!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_outf(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask, at::Tensor & out0, at::Tensor & out1, at::Tensor & out2) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask, out0, out1, out2);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_outf(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, at::IntArrayRef padding, at::IntArrayRef stride, at::IntArrayRef dilation, int64_t groups, ::std::array<bool,3> output_mask, at::Tensor & out0, at::Tensor & out1, at::Tensor & out2) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(dilation), groups, output_mask, out0, out1, out2);
  }
}

// aten::mps_convolution_backward.out(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2) -> (Tensor(a!), Tensor(b!), Tensor(c!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_symint_out(at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask, out0, out1, out2);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_out(at::Tensor & out0, at::Tensor & out1, at::Tensor & out2, const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask, out0, out1, out2);
  }
}

// aten::mps_convolution_backward.out(Tensor self, Tensor grad_output, Tensor weight, SymInt[] padding, SymInt[] stride, SymInt[] dilation, SymInt groups, bool[3] output_mask, *, Tensor(a!) out0, Tensor(b!) out1, Tensor(c!) out2) -> (Tensor(a!), Tensor(b!), Tensor(c!))
inline ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_symint_outf(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask, at::Tensor & out0, at::Tensor & out1, at::Tensor & out2) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask, out0, out1, out2);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  ::std::tuple<at::Tensor &,at::Tensor &,at::Tensor &> mps_convolution_backward_outf(const at::Tensor & self, const at::Tensor & grad_output, const at::Tensor & weight, c10::SymIntArrayRef padding, c10::SymIntArrayRef stride, c10::SymIntArrayRef dilation, c10::SymInt groups, ::std::array<bool,3> output_mask, at::Tensor & out0, at::Tensor & out1, at::Tensor & out2) {
    return at::_ops::mps_convolution_backward_out::call(self, grad_output, weight, padding, stride, dilation, groups, output_mask, out0, out1, out2);
  }
}

}
