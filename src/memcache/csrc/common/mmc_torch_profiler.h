/*
 * Copyright (c) Huawei Technologies Co., Ltd. 2025-2025. All rights reserved.
 * MemCache_Hybrid is licensed under Mulan PSL v2.
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *          http://license.coscl.org.cn/MulanPSL2
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
*/
#ifndef MEMFABRIC_HYBRID_MMC_TORCH_PROFILER_H
#define MEMFABRIC_HYBRID_MMC_TORCH_PROFILER_H

#ifdef MMC_ENABLE_TORCH_PROFILER
#include <ATen/record_function.h>
#include <vector>

#define MMC_RECORD_FUNCTION(name) RECORD_FUNCTION(name, std::vector<c10::IValue>())
#else
#define MMC_RECORD_FUNCTION(name) ((void)0)
#endif

#endif
