#pragma once
// @generated by torchgen/gen.py from DispatchKeyFunction.h

// NB: The implementing C++ file is RegisterDispatchKey.cpp

// The only #includes we need are for custom classes that have defaults in the C++ API
#include <c10/core/MemoryFormat.h>
#include <c10/core/Scalar.h>
#include <ATen/core/Reduction.h>

// Forward declarations of any types needed in the operator signatures.
// We can't directly include these classes because it will cause circular include dependencies.
// This file is included by TensorBody.h, which defines the Tensor class.
#include <ATen/core/ATen_fwd.h>

namespace at {

namespace cuda {

TORCH_API at::Tensor _segment_reduce_backward(const at::Tensor & grad, const at::Tensor & output, const at::Tensor & data, c10::string_view reduce, const ::std::optional<at::Tensor> & lengths={}, const ::std::optional<at::Tensor> & offsets={}, int64_t axis=0, const ::std::optional<at::Scalar> & initial=::std::nullopt);

} // namespace cuda
} // namespace at
