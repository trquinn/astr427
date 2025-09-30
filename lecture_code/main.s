	.file	"main.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC1:
	.string	"%f %f\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB11:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movsd	.LC0(%rip), %xmm2
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%r12
	pushq	%rbx
	.cfi_offset 12, -24
	.cfi_offset 3, -32
	subq	$3200, %rsp
	movq	%rsp, %rbx
	leaq	3200(%rbx), %r12
	jmp	.L4
	.p2align 4,,10
	.p2align 3
.L2:
	addq	$32, %rbx
	cmpq	%r12, %rbx
	je	.L9
.L4:
	movsd	(%rbx), %xmm0
	subsd	8(%rbx), %xmm0
	comisd	%xmm0, %xmm2
	jbe	.L2
	movsd	16(%rbx), %xmm0
	movsd	24(%rbx), %xmm1
	movl	$.LC1, %edi
	movl	$2, %eax
	addq	$32, %rbx
	call	printf
	movsd	.LC0(%rip), %xmm2
	cmpq	%r12, %rbx
	jne	.L4
.L9:
	leaq	-16(%rbp), %rsp
	xorl	%eax, %eax
	popq	%rbx
	popq	%r12
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE11:
	.size	main, .-main
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC0:
	.long	0
	.long	1073741824
	.ident	"GCC: (GNU) 13.2.1 20231205 (Red Hat 13.2.1-6)"
	.section	.note.GNU-stack,"",@progbits
