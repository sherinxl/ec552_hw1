module or_gate (input a, b, output out);

	wire \$n4_0;

	nor (\$n4_0, a, b);
	not (out, \$n4_0);

endmodule
