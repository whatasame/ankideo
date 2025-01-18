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

TORCH_API at::Tensor & _empty_affine_quantized_out(at::Tensor & out, at::IntArrayRef size, double scale=1, int64_t zero_point=0, ::std::optional<at::MemoryFormat> memory_format=c10::MemoryFormat::Contiguous);
TORCH_API at::Tensor & _empty_affine_quantized_outf(at::IntArrayRef size, double scale, int64_t zero_point, ::std::optional<at::MemoryFormat> memory_format, at::Tensor & out);
TORCH_API at::Tensor & _empty_affine_quantized_symint_out(at::Tensor & out, c10::SymIntArrayRef size, double scale=1, int64_t zero_point=0, ::std::optional<at::MemoryFormat> memory_format=c10::MemoryFormat::Contiguous);
TORCH_API at::Tensor & _empty_affine_quantized_symint_outf(c10::SymIntArrayRef size, double scale, int64_t zero_point, ::std::optional<at::MemoryFormat> memory_format, at::Tensor & out);

} // namespace compositeexplicitautograd
} // namespace at
