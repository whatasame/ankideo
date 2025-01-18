#pragma once

// @generated by torchgen/gen.py from NativeFunction.h

#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <optional>
#include <c10/core/QScheme.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <tuple>
#include <vector>


namespace at {
namespace native {
TORCH_API at::Tensor range(const at::Scalar & start, const at::Scalar & end, const at::Scalar & step=1, ::std::optional<at::ScalarType> dtype={}, ::std::optional<at::Layout> layout={}, ::std::optional<at::Device> device={}, ::std::optional<bool> pin_memory={});
TORCH_API at::Tensor & range_out(const at::Scalar & start, const at::Scalar & end, const at::Scalar & step, at::Tensor & out);
TORCH_API at::Tensor & range_cuda_out(const at::Scalar & start, const at::Scalar & end, const at::Scalar & step, at::Tensor & out);
TORCH_API at::Tensor & range_mps_out(const at::Scalar & start, const at::Scalar & end, const at::Scalar & step, at::Tensor & out);
TORCH_API at::Tensor range(const at::Scalar & start, const at::Scalar & end, ::std::optional<at::ScalarType> dtype={}, ::std::optional<at::Layout> layout={}, ::std::optional<at::Device> device={}, ::std::optional<bool> pin_memory={});
TORCH_API at::Tensor & range_out_no_step(const at::Scalar & start, const at::Scalar & end, at::Tensor & out);
} // namespace native
} // namespace at
