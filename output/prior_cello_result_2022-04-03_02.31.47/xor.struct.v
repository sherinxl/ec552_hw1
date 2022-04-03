module and_gate (input a, b, output out);

	wire \$n5_0;
	wire \$n6_0;
	wire \$n4_0;
	wire \$n7_0;

	not (\$n4_0, a);
	not (\$n5_0, b);
	nor (\$n7_0, \$n5_0, \$n4_0);
	nor (\$n6_0, a, b);
	nor (out, \$n6_0, \$n7_0);

endmodule
