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
TORCH_API at::Tensor copy_sparse_to_sparse(const at::Tensor & self, const at::Tensor & src, bool non_blocking=false);
TORCH_API at::Tensor & copy_sparse_to_sparse_out(const at::Tensor & self, const at::Tensor & src, bool non_blocking, at::Tensor & out);
TORCH_API at::Tensor & copy_sparse_(at::Tensor & self, const at::Tensor & src, bool non_blocking=false);
} // namespace native
} // namespace at
