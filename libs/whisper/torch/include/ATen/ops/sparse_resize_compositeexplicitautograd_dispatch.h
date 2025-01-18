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

namespace compositeexplicitautograd {

TORCH_API at::Tensor sparse_resize(const at::Tensor & self, at::IntArrayRef size, int64_t sparse_dim, int64_t dense_dim);
TORCH_API const at::Tensor & sparse_resize_out(const at::Tensor & out, const at::Tensor & self, at::IntArrayRef size, int64_t sparse_dim, int64_t dense_dim);
TORCH_API const at::Tensor & sparse_resize_outf(const at::Tensor & self, at::IntArrayRef size, int64_t sparse_dim, int64_t dense_dim, const at::Tensor & out);

} // namespace compositeexplicitautograd
} // namespace at
