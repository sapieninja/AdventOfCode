	.file	"21.c"
	.text
	.p2align 4
	.globl	amalgamate
	.type	amalgamate, @function
amalgamate:
.LFB23:
	.cfi_startproc
	endbr64
	imull	$100000, %ecx, %ecx
	leal	(%rsi,%rsi,4), %eax
	leal	(%rdi,%rax,2), %esi
	imull	$1000, %edx, %eax
	addl	%esi, %eax
	addl	%ecx, %eax
	ret
	.cfi_endproc
.LFE23:
	.size	amalgamate, .-amalgamate
	.p2align 4
	.globl	noways
	.type	noways, @function
noways:
.LFB24:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	imull	$1000, %edx, %r14d
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	subq	$104, %rsp
	.cfi_def_cfa_offset 160
	movq	160(%rsp), %rax
	movl	%edi, 20(%rsp)
	movl	%edx, 16(%rsp)
	movq	%r8, 40(%rsp)
	movq	%r9, 48(%rsp)
	movq	%rax, 8(%rsp)
	movq	%fs:40, %rax
	movq	%rax, 88(%rsp)
	xorl	%eax, %eax
	leal	(%rsi,%rsi,4), %eax
	leal	(%rdi,%rax,2), %eax
	leaq	cachea(%rip), %rdi
	addl	%r14d, %eax
	imull	$100000, %ecx, %r14d
	addl	%eax, %r14d
	movslq	%r14d, %rax
	movq	%rax, 32(%rsp)
	movq	(%rdi,%rax,8), %rax
	testq	%rax, %rax
	jne	.L16
	movq	32(%rsp), %rbx
	leaq	cacheb(%rip), %rdi
	movq	%rdi, 56(%rsp)
	movq	(%rdi,%rbx,8), %r15
	testq	%r15, %r15
	jne	.L4
	cmpl	$39, 16(%rsp)
	jg	.L11
	cmpl	$39, %ecx
	jg	.L11
	movq	8(%rsp), %rax
	leaq	80(%rsp), %r13
	movq	%r15, %rbp
	movl	%esi, %r12d
	leaq	72(%rsp), %r9
	movq	%r13, %r8
	xorl	%r14d, %r14d
	movl	%ecx, %r13d
	movq	%rax, %rbx
	addq	$108, %rax
	movq	%r9, %r15
	movq	%rax, 24(%rsp)
	.p2align 4,,10
	.p2align 3
.L9:
	movl	20(%rsp), %edx
	addl	(%rbx), %edx
	subq	$8, %rsp
	.cfi_def_cfa_offset 168
	movq	%r15, %r9
	subl	$1, %edx
	movl	24(%rsp), %eax
	pushq	16(%rsp)
	.cfi_def_cfa_offset 176
	movl	%r12d, %edi
	movslq	%edx, %rsi
	movl	%edx, %ecx
	addq	$4, %rbx
	imulq	$1717986919, %rsi, %rsi
	sarl	$31, %ecx
	movq	%r8, 16(%rsp)
	sarq	$34, %rsi
	subl	%ecx, %esi
	leal	(%rsi,%rsi,4), %ecx
	addl	%ecx, %ecx
	subl	%ecx, %edx
	movl	%edx, %esi
	leal	1(%rdx,%rax), %ecx
	movl	%r13d, %edx
	addl	$1, %esi
	call	noways
	addq	88(%rsp), %rbp
	addq	96(%rsp), %r14
	popq	%rax
	.cfi_def_cfa_offset 168
	popq	%rdx
	.cfi_def_cfa_offset 160
	cmpq	%rbx, 24(%rsp)
	movq	(%rsp), %r8
	jne	.L9
	movq	40(%rsp), %rax
	movq	56(%rsp), %rbx
	leaq	cachea(%rip), %rdi
	movq	%rbp, (%rax)
	movq	48(%rsp), %rax
	movq	%r14, (%rax)
	movq	32(%rsp), %rax
	movq	%rbp, (%rdi,%rax,8)
	movq	%r14, (%rbx,%rax,8)
	jmp	.L3
	.p2align 4,,10
	.p2align 3
.L16:
	leaq	cacheb(%rip), %rbx
	movq	%rbx, 56(%rsp)
.L4:
	movq	40(%rsp), %rdi
	movq	%rax, (%rdi)
	movq	32(%rsp), %rdi
	movq	56(%rsp), %rax
	movq	(%rax,%rdi,8), %rax
	movq	48(%rsp), %rdi
	movq	%rax, (%rdi)
.L3:
	movq	88(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L17
	addq	$104, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 56
	popq	%rbx
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
	.p2align 4,,10
	.p2align 3
.L11:
	.cfi_restore_state
	movq	40(%rsp), %rax
	leaq	cachea(%rip), %rdi
	movq	$1, (%rax)
	movq	48(%rsp), %rax
	movq	$0, (%rax)
	movq	32(%rsp), %rax
	movq	$1, (%rdi,%rax,8)
	movq	56(%rsp), %rdi
	movq	$0, (%rdi,%rax,8)
	jmp	.L3
.L17:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE24:
	.size	noways, .-noways
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC6:
	.string	"%ld\n"
.LC8:
	.string	"%f\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB25:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$152, %rsp
	.cfi_def_cfa_offset 176
	movdqa	.LC0(%rip), %xmm0
	movq	%fs:40, %rax
	movq	%rax, 136(%rsp)
	xorl	%eax, %eax
	movl	$9, 120(%rsp)
	movabsq	$34359738376, %rax
	movaps	%xmm0, 16(%rsp)
	movdqa	.LC1(%rip), %xmm0
	movq	%rax, 112(%rsp)
	movaps	%xmm0, 32(%rsp)
	movdqa	.LC2(%rip), %xmm0
	movaps	%xmm0, 48(%rsp)
	movdqa	.LC3(%rip), %xmm0
	movaps	%xmm0, 64(%rsp)
	movdqa	.LC4(%rip), %xmm0
	movaps	%xmm0, 80(%rsp)
	movdqa	.LC5(%rip), %xmm0
	movaps	%xmm0, 96(%rsp)
	call	clock@PLT
	subq	$8, %rsp
	.cfi_def_cfa_offset 184
	xorl	%ecx, %ecx
	xorl	%edx, %edx
	movq	%rax, %rbp
	leaq	24(%rsp), %rax
	movl	$1, %esi
	movl	$10, %edi
	pushq	%rax
	.cfi_def_cfa_offset 192
	leaq	16(%rsp), %r8
	leaq	24(%rsp), %r9
	call	noways
	call	clock@PLT
	movq	16(%rsp), %r8
	movq	24(%rsp), %rdx
	movq	%rax, %rbx
	popq	%rax
	.cfi_def_cfa_offset 184
	popq	%rcx
	.cfi_def_cfa_offset 176
	cmpq	%rdx, %r8
	jg	.L23
.L19:
	cmpq	%r8, %rdx
	jg	.L24
.L20:
	subq	%rbp, %rbx
	pxor	%xmm0, %xmm0
	movl	$1, %edi
	movl	$1, %eax
	cvtsi2sdq	%rbx, %xmm0
	mulsd	.LC7(%rip), %xmm0
	leaq	.LC8(%rip), %rsi
	call	__printf_chk@PLT
	movq	136(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L25
	addq	$152, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	xorl	%eax, %eax
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
.L23:
	.cfi_restore_state
	movq	%r8, %rdx
	leaq	.LC6(%rip), %rsi
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	movq	8(%rsp), %rdx
	movq	(%rsp), %r8
	jmp	.L19
.L24:
	leaq	.LC6(%rip), %rsi
	movl	$1, %edi
	xorl	%eax, %eax
	call	__printf_chk@PLT
	jmp	.L20
.L25:
	call	__stack_chk_fail@PLT
	.cfi_endproc
.LFE25:
	.size	main, .-main
	.globl	cacheb
	.bss
	.align 32
	.type	cacheb, @object
	.size	cacheb, 80000000
cacheb:
	.zero	80000000
	.globl	cachea
	.align 32
	.type	cachea, @object
	.size	cachea, 80000000
cachea:
	.zero	80000000
	.section	.rodata.cst16,"aM",@progbits,16
	.align 16
.LC0:
	.long	3
	.long	4
	.long	4
	.long	4
	.align 16
.LC1:
	.long	5
	.long	5
	.long	5
	.long	5
	.align 16
.LC2:
	.long	5
	.long	5
	.long	6
	.long	6
	.align 16
.LC3:
	.long	6
	.long	6
	.long	6
	.long	6
	.align 16
.LC4:
	.long	6
	.long	7
	.long	7
	.long	7
	.align 16
.LC5:
	.long	7
	.long	7
	.long	7
	.long	8
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC7:
	.long	-1598689907
	.long	1051772663
	.ident	"GCC: (Ubuntu 10.3.0-1ubuntu1) 10.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
