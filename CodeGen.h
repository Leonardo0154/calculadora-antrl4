#pragma once
#include <memory>
#include <string>
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/LLVMContext.h"

struct CodeGen {
    llvm::LLVMContext context;
    std::unique_ptr<llvm::Module> module;
    llvm::IRBuilder<> builder;

    CodeGen(const std::string &moduleName);
    llvm::Function *createMain();
    llvm::AllocaInst *createEntryBlockAlloca(llvm::Function *func, const std::string &varName, llvm::Type *type);
    llvm::Value* castToDoubleIfNeeded(llvm::Value* v);
};