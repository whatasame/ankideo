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



#include <ATen/ops/cudnn_convolution_add_relu_ops.h>

namespace at {


// aten::cudnn_convolution_add_relu(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups) -> Tensor
inline at::Tensor cudnn_convolution_add_relu(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups) {
    return at::_ops::cudnn_convolution_add_relu::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  at::Tensor cudnn_convolution_add_relu(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups) {
    return at::_ops::cudnn_convolution_add_relu::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups);
  }
}

// aten::cudnn_convolution_add_relu(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups) -> Tensor
inline at::Tensor cudnn_convolution_add_relu_symint(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups) {
    return at::_ops::cudnn_convolution_add_relu::call(self, weight, z, alpha, bias, stride, padding, dilation, groups);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  at::Tensor cudnn_convolution_add_relu(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups) {
    return at::_ops::cudnn_convolution_add_relu::call(self, weight, z, alpha, bias, stride, padding, dilation, groups);
  }
}

// aten::cudnn_convolution_add_relu.out(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & cudnn_convolution_add_relu_out(at::Tensor & out, const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups, out);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  at::Tensor & cudnn_convolution_add_relu_out(at::Tensor & out, const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups, out);
  }
}

// aten::cudnn_convolution_add_relu.out(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & cudnn_convolution_add_relu_outf(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups, at::Tensor & out) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups, out);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, int64_t>::value>>
  at::Tensor & cudnn_convolution_add_relu_outf(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, int64_t groups, at::Tensor & out) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, c10::fromIntArrayRefSlow(stride), c10::fromIntArrayRefSlow(padding), c10::fromIntArrayRefSlow(dilation), groups, out);
  }
}

// aten::cudnn_convolution_add_relu.out(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & cudnn_convolution_add_relu_symint_out(at::Tensor & out, const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, stride, padding, dilation, groups, out);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  at::Tensor & cudnn_convolution_add_relu_out(at::Tensor & out, const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, stride, padding, dilation, groups, out);
  }
}

// aten::cudnn_convolution_add_relu.out(Tensor self, Tensor weight, Tensor z, Scalar? alpha, Tensor? bias, SymInt[] stride, SymInt[] padding, SymInt[] dilation, SymInt groups, *, Tensor(a!) out) -> Tensor(a!)
inline at::Tensor & cudnn_convolution_add_relu_symint_outf(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups, at::Tensor & out) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, stride, padding, dilation, groups, out);
}
namespace symint {
  template <typename T, typename = std::enable_if_t<std::is_same<T, c10::SymInt>::value>>
  at::Tensor & cudnn_convolution_add_relu_outf(const at::Tensor & self, const at::Tensor & weight, const at::Tensor & z, const ::std::optional<at::Scalar> & alpha, const ::std::optional<at::Tensor> & bias, c10::SymIntArrayRef stride, c10::SymIntArrayRef padding, c10::SymIntArrayRef dilation, c10::SymInt groups, at::Tensor & out) {
    return at::_ops::cudnn_convolution_add_relu_out::call(self, weight, z, alpha, bias, stride, padding, dilation, groups, out);
  }
}

}
