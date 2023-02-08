from spec2json.spec import Section

# https://tc39.es/ecma262/#sec-math-object
ECMA262_MATH_OBJECT_HTML = """
<emu-clause id="sec-math-object">
  <h1><span class="secnum">21.3</span> The Math Object</h1>
  <p>The Math object:</p>
  <ul>
    <li>is <dfn>%Math%</dfn>.</li>
    <li>is the initial value of the <emu-val>"Math"</emu-val> property of the <emu-xref href="#sec-global-object" id="_ref_9395"><a href="#sec-global-object">global object</a></emu-xref>.</li>
    <li>is an <emu-xref href="#ordinary-object" id="_ref_9396"><a href="#ordinary-object">ordinary object</a></emu-xref>.</li>
    <li>has a [[Prototype]] internal slot whose value is <emu-xref href="#sec-properties-of-the-object-prototype-object" id="_ref_9397"><a href="#sec-properties-of-the-object-prototype-object">%Object.prototype%</a></emu-xref>.</li>
    <li>is not a <emu-xref href="#function-object" id="_ref_9398"><a href="#function-object">function object</a></emu-xref>.</li>
    <li>does not have a [[Construct]] internal method; it cannot be used as a <emu-xref href="#constructor" id="_ref_9399"><a href="#constructor">constructor</a></emu-xref> with the <code>new</code> operator.</li>
    <li>does not have a [[Call]] internal method; it cannot be invoked as a function.</li>
  </ul>
  <emu-note><span class="note">Note</span><div class="note-contents">
    <p>In this specification, the phrase “the <emu-xref href="#number-value-for" id="_ref_9400"><a href="#number-value-for">Number value for</a></emu-xref> <var>x</var>” has a technical meaning defined in <emu-xref href="#sec-ecmascript-language-types-number-type" id="_ref_625"><a href="#sec-ecmascript-language-types-number-type">6.1.6.1</a></emu-xref>.</p>
  </div></emu-note>

  <emu-clause id="sec-value-properties-of-the-math-object">
    <h1><span class="secnum">21.3.1</span> Value Properties of the Math Object</h1>

    <emu-clause id="sec-math.e">
      <h1><span class="secnum">21.3.1.1</span> Math.E</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9401"><a href="#number-value-for">Number value for</a></emu-xref> <var>e</var>, the base of the natural logarithms, which is approximately 2.7182818284590452354.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
    </emu-clause>

    <emu-clause id="sec-math.ln10">
      <h1><span class="secnum">21.3.1.2</span> Math.LN10</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9402"><a href="#number-value-for">Number value for</a></emu-xref> the natural logarithm of 10, which is approximately 2.302585092994046.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
    </emu-clause>

    <emu-clause id="sec-math.ln2">
      <h1><span class="secnum">21.3.1.3</span> Math.LN2</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9403"><a href="#number-value-for">Number value for</a></emu-xref> the natural logarithm of 2, which is approximately 0.6931471805599453.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
    </emu-clause>

    <emu-clause id="sec-math.log10e">
      <h1><span class="secnum">21.3.1.4</span> Math.LOG10E</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9404"><a href="#number-value-for">Number value for</a></emu-xref> the base-10 logarithm of <var>e</var>, the base of the natural logarithms; this value is approximately 0.4342944819032518.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.LOG10E</code> is approximately the reciprocal of the value of <code>Math.LN10</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.log2e">
      <h1><span class="secnum">21.3.1.5</span> Math.LOG2E</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9405"><a href="#number-value-for">Number value for</a></emu-xref> the base-2 logarithm of <var>e</var>, the base of the natural logarithms; this value is approximately 1.4426950408889634.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.LOG2E</code> is approximately the reciprocal of the value of <code>Math.LN2</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.pi">
      <h1><span class="secnum">21.3.1.6</span> Math.PI</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9406"><a href="#number-value-for">Number value for</a></emu-xref> π, the ratio of the circumference of a circle to its diameter, which is approximately 3.1415926535897932.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
    </emu-clause>

    <emu-clause id="sec-math.sqrt1_2">
      <h1><span class="secnum">21.3.1.7</span> Math.SQRT1_2</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9407"><a href="#number-value-for">Number value for</a></emu-xref> the square root of ½, which is approximately 0.7071067811865476.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.SQRT1_2</code> is approximately the reciprocal of the value of <code>Math.SQRT2</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.sqrt2">
      <h1><span class="secnum">21.3.1.8</span> Math.SQRT2</h1>
      <p>The <emu-xref href="#number-value-for" id="_ref_9408"><a href="#number-value-for">Number value for</a></emu-xref> the square root of 2, which is approximately 1.4142135623730951.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>false</emu-val> }.</p>
    </emu-clause>

    <emu-clause id="sec-math-@@tostringtag">
      <h1><span class="secnum">21.3.1.9</span> Math [ @@toStringTag ]</h1>
      <p>The initial value of the <emu-xref href="#sec-well-known-symbols" id="_ref_9409"><a href="#sec-well-known-symbols">@@toStringTag</a></emu-xref> property is the String value <emu-val>"Math"</emu-val>.</p>
      <p>This property has the attributes { [[Writable]]: <emu-val>false</emu-val>, [[Enumerable]]: <emu-val>false</emu-val>, [[Configurable]]: <emu-val>true</emu-val> }.</p>
    </emu-clause>
  </emu-clause>

  <emu-clause id="sec-function-properties-of-the-math-object">
    <h1><span class="secnum">21.3.2</span> Function Properties of the Math Object</h1>
    <emu-note><span class="note">Note</span><div class="note-contents">
      <p>The behaviour of the functions <code>acos</code>, <code>acosh</code>, <code>asin</code>, <code>asinh</code>, <code>atan</code>, <code>atanh</code>, <code>atan2</code>, <code>cbrt</code>, <code>cos</code>, <code>cosh</code>, <code>exp</code>, <code>expm1</code>, <code>hypot</code>, <code>log</code>, <code>log1p</code>, <code>log2</code>, <code>log10</code>, <code>pow</code>, <code>random</code>, <code>sin</code>, <code>sinh</code>, <code>sqrt</code>, <code>tan</code>, and <code>tanh</code> is not precisely specified here except to require specific results for certain argument values that represent boundary cases of interest. For other argument values, these functions are intended to compute approximations to the results of familiar mathematical functions, but some latitude is allowed in the choice of approximation algorithms. The general intent is that an implementer should be able to use the same mathematical library for ECMAScript on a given hardware platform that is available to C programmers on that platform.</p>
      <p>Although the choice of algorithms is left to the implementation, it is recommended (but not specified by this standard) that implementations use the approximation algorithms for <emu-xref href="#sec-bibliography" id="_ref_9410"><a href="#sec-bibliography">IEEE 754-2019</a></emu-xref> arithmetic contained in <code>fdlibm</code>, the freely distributable mathematical library from Sun Microsystems (<a href="http://www.netlib.org/fdlibm">http://www.netlib.org/fdlibm</a>).</p>
    </div></emu-note>

    <emu-clause id="sec-math.abs">
      <h1><span class="secnum">21.3.2.1</span> Math.abs ( <var>x</var> )</h1>
      <p>This function returns the absolute value of <var>x</var>; the result has the same magnitude as <var>x</var> but has positive sign.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9411"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>+∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return -<var>n</var>.</li><li>Return <var>n</var>.</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.acos">
      <h1><span class="secnum">21.3.2.2</span> Math.acos ( <var>x</var> )</h1>
      <p>This function returns the inverse cosine of <var>x</var>. The result is expressed in radians and is in the <emu-xref href="#inclusive-interval" id="_ref_9412"><a href="#inclusive-interval">inclusive interval</a></emu-xref> from <emu-val>+0</emu-val><sub>𝔽</sub> to <emu-xref aoid="𝔽" id="_ref_9413"><a href="#𝔽">𝔽</a></emu-xref>(π).</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9414"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is <emu-val>NaN</emu-val>, <var>n</var> &gt; <emu-val>1</emu-val><sub>𝔽</sub>, or <var>n</var> &lt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9415"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse cosine of <emu-xref aoid="ℝ" id="_ref_9416"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.acosh">
      <h1><span class="secnum">21.3.2.3</span> Math.acosh ( <var>x</var> )</h1>
      <p>This function returns the inverse hyperbolic cosine of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9417"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is either <emu-val>NaN</emu-val> or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9418"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse hyperbolic cosine of <emu-xref aoid="ℝ" id="_ref_9419"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.asin">
      <h1><span class="secnum">21.3.2.4</span> Math.asin ( <var>x</var> )</h1>
      <p>This function returns the inverse sine of <var>x</var>. The result is expressed in radians and is in the <emu-xref href="#inclusive-interval" id="_ref_9420"><a href="#inclusive-interval">inclusive interval</a></emu-xref> from <emu-xref aoid="𝔽" id="_ref_9421"><a href="#𝔽">𝔽</a></emu-xref>(-π / 2) to <emu-xref aoid="𝔽" id="_ref_9422"><a href="#𝔽">𝔽</a></emu-xref>(π / 2).</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9423"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &gt; <emu-val>1</emu-val><sub>𝔽</sub> or <var>n</var> &lt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9424"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse sine of <emu-xref aoid="ℝ" id="_ref_9425"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.asinh">
      <h1><span class="secnum">21.3.2.5</span> Math.asinh ( <var>x</var> )</h1>
      <p>This function returns the inverse hyperbolic sine of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9426"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9427"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9428"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse hyperbolic sine of <emu-xref aoid="ℝ" id="_ref_9429"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.atan">
      <h1><span class="secnum">21.3.2.6</span> Math.atan ( <var>x</var> )</h1>
      <p>This function returns the inverse tangent of <var>x</var>. The result is expressed in radians and is in the <emu-xref href="#inclusive-interval" id="_ref_9430"><a href="#inclusive-interval">inclusive interval</a></emu-xref> from <emu-xref aoid="𝔽" id="_ref_9431"><a href="#𝔽">𝔽</a></emu-xref>(-π / 2) to <emu-xref aoid="𝔽" id="_ref_9432"><a href="#𝔽">𝔽</a></emu-xref>(π / 2).</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9433"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9434"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π / 2.</li><li>If <var>n</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9435"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π / 2.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9436"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse tangent of <emu-xref aoid="ℝ" id="_ref_9437"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.atanh">
      <h1><span class="secnum">21.3.2.7</span> Math.atanh ( <var>x</var> )</h1>
      <p>This function returns the inverse hyperbolic tangent of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9438"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &gt; <emu-val>1</emu-val><sub>𝔽</sub> or <var>n</var> &lt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9439"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse hyperbolic tangent of <emu-xref aoid="ℝ" id="_ref_9440"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.atan2">
      <h1><span class="secnum">21.3.2.8</span> Math.atan2 ( <var>y</var>, <var>x</var> )</h1>
      <p>This function returns the inverse tangent of the quotient <emu-eqn class="inline"><var>y</var> / <var>x</var></emu-eqn> of the arguments <var>y</var> and <var>x</var>, where the signs of <var>y</var> and <var>x</var> are used to determine the quadrant of the result. Note that it is intentional and traditional for the two-argument inverse tangent function that the argument named <var>y</var> be first and the argument named <var>x</var> be second. The result is expressed in radians and is in the <emu-xref href="#inclusive-interval" id="_ref_9441"><a href="#inclusive-interval">inclusive interval</a></emu-xref> from -π to +π.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>ny</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9442"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>y</var>).</li><li>Let <var>nx</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9443"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>ny</var> is <emu-val>NaN</emu-val> or <var>nx</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>ny</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9444"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π / 4.</li><li>If <var>nx</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9445"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing 3π / 4.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9446"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π / 2.</li></ol></li><li>If <var>ny</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9447"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π / 4.</li><li>If <var>nx</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9448"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -3π / 4.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9449"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π / 2.</li></ol></li><li>If <var>ny</var> is <emu-val>+0</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub> or <var>nx</var> is <emu-val>+0</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9450"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π.</li></ol></li><li>If <var>ny</var> is <emu-val>-0</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub> or <var>nx</var> is <emu-val>+0</emu-val><sub>𝔽</sub>, return <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9451"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π.</li></ol></li><li><emu-xref href="#assert" id="_ref_9452"><a href="#assert">Assert</a></emu-xref>: <var>ny</var> is <emu-xref href="#finite" id="_ref_9453"><a href="#finite">finite</a></emu-xref> and is neither <emu-val>+0</emu-val><sub>𝔽</sub> nor <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>If <var>ny</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>nx</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9454"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π.</li><li>If <var>nx</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9455"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing π / 2.</li></ol></li><li>If <var>ny</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, then<ol><li>If <var>nx</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>If <var>nx</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9456"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π.</li><li>If <var>nx</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return an <emu-xref href="#implementation-approximated" id="_ref_9457"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing -π / 2.</li></ol></li><li><emu-xref href="#assert" id="_ref_9458"><a href="#assert">Assert</a></emu-xref>: <var>nx</var> is <emu-xref href="#finite" id="_ref_9459"><a href="#finite">finite</a></emu-xref> and is neither <emu-val>+0</emu-val><sub>𝔽</sub> nor <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9460"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the inverse tangent of the quotient <emu-xref aoid="ℝ" id="_ref_9461"><a href="#ℝ">ℝ</a></emu-xref>(<var>ny</var>) / <emu-xref aoid="ℝ" id="_ref_9462"><a href="#ℝ">ℝ</a></emu-xref>(<var>nx</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.cbrt">
      <h1><span class="secnum">21.3.2.9</span> Math.cbrt ( <var>x</var> )</h1>
      <p>This function returns the cube root of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9463"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9464"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9465"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the cube root of <emu-xref aoid="ℝ" id="_ref_9466"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.ceil">
      <h1><span class="secnum">21.3.2.10</span> Math.ceil ( <var>x</var> )</h1>
      <p>This function returns the smallest (closest to -∞) <emu-xref href="#integral-number" id="_ref_9467"><a href="#integral-number">integral Number</a></emu-xref> value that is not less than <var>x</var>. If <var>x</var> is already an <emu-xref href="#integral-number" id="_ref_9468"><a href="#integral-number">integral Number</a></emu-xref>, the result is <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9469"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9470"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub> and <var>n</var> &gt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is an <emu-xref href="#integral-number" id="_ref_9471"><a href="#integral-number">integral Number</a></emu-xref>, return <var>n</var>.</li><li>Return the smallest (closest to -∞) <emu-xref href="#integral-number" id="_ref_9472"><a href="#integral-number">integral Number</a></emu-xref> value that is not less than <var>n</var>.</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.ceil(x)</code> is the same as the value of <code>-Math.floor(-x)</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.clz32">
      <h1><span class="secnum">21.3.2.11</span> Math.clz32 ( <var>x</var> )</h1>
      <p>This function performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToUint32" id="_ref_9473"><a href="#sec-touint32" class="e-user-code">ToUint32</a></emu-xref>(<var>x</var>).</li><li>Let <var>p</var> be the number of leading zero bits in the unsigned 32-bit binary representation of <var>n</var>.</li><li>Return <emu-xref aoid="𝔽" id="_ref_9474"><a href="#𝔽">𝔽</a></emu-xref>(<var>p</var>).</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, this method returns <emu-val>32</emu-val><sub>𝔽</sub>. If the most significant bit of the 32-bit binary encoding of <var>n</var> is 1, this method returns <emu-val>+0</emu-val><sub>𝔽</sub>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.cos">
      <h1><span class="secnum">21.3.2.12</span> Math.cos ( <var>x</var> )</h1>
      <p>This function returns the cosine of <var>x</var>. The argument is expressed in radians.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9475"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9476"><a href="#finite">finite</a></emu-xref>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>1</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9477"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the cosine of <emu-xref aoid="ℝ" id="_ref_9478"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.cosh">
      <h1><span class="secnum">21.3.2.13</span> Math.cosh ( <var>x</var> )</h1>
      <p>This function returns the hyperbolic cosine of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9479"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is either <emu-val>+∞</emu-val><sub>𝔽</sub> or <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>+∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>1</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9480"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the hyperbolic cosine of <emu-xref aoid="ℝ" id="_ref_9481"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.cosh(x)</code> is the same as the value of <code>(Math.exp(x) + Math.exp(-x)) / 2</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.exp">
      <h1><span class="secnum">21.3.2.14</span> Math.exp ( <var>x</var> )</h1>
      <p>This function returns the exponential function of <var>x</var> (<var>e</var> raised to the power of <var>x</var>, where <var>e</var> is the base of the natural logarithms).</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9482"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is either <emu-val>NaN</emu-val> or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>1</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9483"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the exponential function of <emu-xref aoid="ℝ" id="_ref_9484"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.expm1">
      <h1><span class="secnum">21.3.2.15</span> Math.expm1 ( <var>x</var> )</h1>
      <p>This function returns the result of subtracting 1 from the exponential function of <var>x</var> (<var>e</var> raised to the power of <var>x</var>, where <var>e</var> is the base of the natural logarithms). The result is computed in a way that is accurate even when the value of <var>x</var> is close to 0.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9485"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, <emu-val>-0</emu-val><sub>𝔽</sub>, or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>-1</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9486"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of subtracting 1 from the exponential function of <emu-xref aoid="ℝ" id="_ref_9487"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.floor">
      <h1><span class="secnum">21.3.2.16</span> Math.floor ( <var>x</var> )</h1>
      <p>This function returns the greatest (closest to +∞) <emu-xref href="#integral-number" id="_ref_9488"><a href="#integral-number">integral Number</a></emu-xref> value that is not greater than <var>x</var>. If <var>x</var> is already an <emu-xref href="#integral-number" id="_ref_9489"><a href="#integral-number">integral Number</a></emu-xref>, the result is <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9490"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9491"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>1</emu-val><sub>𝔽</sub> and <var>n</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is an <emu-xref href="#integral-number" id="_ref_9492"><a href="#integral-number">integral Number</a></emu-xref>, return <var>n</var>.</li><li>Return the greatest (closest to +∞) <emu-xref href="#integral-number" id="_ref_9493"><a href="#integral-number">integral Number</a></emu-xref> value that is not greater than <var>n</var>.</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.floor(x)</code> is the same as the value of <code>-Math.ceil(-x)</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.fround">
      <h1><span class="secnum">21.3.2.17</span> Math.fround ( <var>x</var> )</h1>
      <p>This function performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9494"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>n</var> is one of <emu-val>+0</emu-val><sub>𝔽</sub>, <emu-val>-0</emu-val><sub>𝔽</sub>, <emu-val>+∞</emu-val><sub>𝔽</sub>, or <emu-val>-∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>Let <var>n32</var> be the result of converting <var>n</var> to a value in <emu-xref href="#sec-bibliography" id="_ref_9495"><a href="#sec-bibliography">IEEE 754-2019</a></emu-xref> binary32 format using roundTiesToEven mode.</li><li>Let <var>n64</var> be the result of converting <var>n32</var> to a value in <emu-xref href="#sec-bibliography" id="_ref_9496"><a href="#sec-bibliography">IEEE 754-2019</a></emu-xref> binary64 format.</li><li>Return the ECMAScript Number value corresponding to <var>n64</var>.</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.hypot">
      <h1><span class="secnum">21.3.2.18</span> Math.hypot ( ...<var>args</var> )</h1>
      <p>Given zero or more arguments, this function returns the square root of the sum of squares of its arguments.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>coerced</var> be a new empty <emu-xref href="#sec-list-and-record-specification-type" id="_ref_9497"><a href="#sec-list-and-record-specification-type">List</a></emu-xref>.</li><li>For each element <var>arg</var> of <var>args</var>, do<ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9498"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>arg</var>).</li><li>Append <var>n</var> to <var>coerced</var>.</li></ol></li><li>For each element <var>number</var> of <var>coerced</var>, do<ol><li>If <var>number</var> is either <emu-val>+∞</emu-val><sub>𝔽</sub> or <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>+∞</emu-val><sub>𝔽</sub>.</li></ol></li><li>Let <var>onlyZero</var> be <emu-val>true</emu-val>.</li><li>For each element <var>number</var> of <var>coerced</var>, do<ol><li>If <var>number</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>number</var> is neither <emu-val>+0</emu-val><sub>𝔽</sub> nor <emu-val>-0</emu-val><sub>𝔽</sub>, set <var>onlyZero</var> to <emu-val>false</emu-val>.</li></ol></li><li>If <var>onlyZero</var> is <emu-val>true</emu-val>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9499"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the square root of the sum of squares of the <emu-xref href="#mathematical-value" id="_ref_9500"><a href="#mathematical-value">mathematical values</a></emu-xref> of the elements of <var>coerced</var>.</li></ol></emu-alg>
      <p>The <emu-val>"length"</emu-val> property of this function is <emu-val>2</emu-val><sub>𝔽</sub>.</p>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>Implementations should take care to avoid the loss of precision from overflows and underflows that are prone to occur in naive implementations when this function is called with two or more arguments.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.imul">
      <h1><span class="secnum">21.3.2.19</span> Math.imul ( <var>x</var>, <var>y</var> )</h1>
      <p>This function performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>a</var> be <emu-xref aoid="ℝ" id="_ref_9501"><a href="#ℝ">ℝ</a></emu-xref>(? <emu-xref aoid="ToUint32" id="_ref_9502"><a href="#sec-touint32" class="e-user-code">ToUint32</a></emu-xref>(<var>x</var>)).</li><li>Let <var>b</var> be <emu-xref aoid="ℝ" id="_ref_9503"><a href="#ℝ">ℝ</a></emu-xref>(? <emu-xref aoid="ToUint32" id="_ref_9504"><a href="#sec-touint32" class="e-user-code">ToUint32</a></emu-xref>(<var>y</var>)).</li><li>Let <var>product</var> be (<var>a</var> × <var>b</var>) <emu-xref aoid="modulo" id="_ref_9505"><a href="#eqn-modulo">modulo</a></emu-xref> 2<sup>32</sup>.</li><li>If <var>product</var> ≥ 2<sup>31</sup>, return <emu-xref aoid="𝔽" id="_ref_9506"><a href="#𝔽">𝔽</a></emu-xref>(<var>product</var> - 2<sup>32</sup>); otherwise return <emu-xref aoid="𝔽" id="_ref_9507"><a href="#𝔽">𝔽</a></emu-xref>(<var>product</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.log">
      <h1><span class="secnum">21.3.2.20</span> Math.log ( <var>x</var> )</h1>
      <p>This function returns the natural logarithm of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9508"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is either <emu-val>NaN</emu-val> or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9509"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the natural logarithm of <emu-xref aoid="ℝ" id="_ref_9510"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.log1p">
      <h1><span class="secnum">21.3.2.21</span> Math.log1p ( <var>x</var> )</h1>
      <p>This function returns the natural logarithm of 1 + <var>x</var>. The result is computed in a way that is accurate even when the value of x is close to zero.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9511"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, <emu-val>-0</emu-val><sub>𝔽</sub>, or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9512"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the natural logarithm of 1 + <emu-xref aoid="ℝ" id="_ref_9513"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.log10">
      <h1><span class="secnum">21.3.2.22</span> Math.log10 ( <var>x</var> )</h1>
      <p>This function returns the base 10 logarithm of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9514"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is either <emu-val>NaN</emu-val> or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9515"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the base 10 logarithm of <emu-xref aoid="ℝ" id="_ref_9516"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.log2">
      <h1><span class="secnum">21.3.2.23</span> Math.log2 ( <var>x</var> )</h1>
      <p>This function returns the base 2 logarithm of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9517"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is either <emu-val>NaN</emu-val> or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>1</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9518"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the base 2 logarithm of <emu-xref aoid="ℝ" id="_ref_9519"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.max">
      <h1><span class="secnum">21.3.2.24</span> Math.max ( ...<var>args</var> )</h1>
      <p>Given zero or more arguments, this function calls <emu-xref aoid="ToNumber" id="_ref_9520"><a href="#sec-tonumber">ToNumber</a></emu-xref> on each of the arguments and returns the largest of the resulting values.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>coerced</var> be a new empty <emu-xref href="#sec-list-and-record-specification-type" id="_ref_9521"><a href="#sec-list-and-record-specification-type">List</a></emu-xref>.</li><li>For each element <var>arg</var> of <var>args</var>, do<ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9522"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>arg</var>).</li><li>Append <var>n</var> to <var>coerced</var>.</li></ol></li><li>Let <var>highest</var> be <emu-val>-∞</emu-val><sub>𝔽</sub>.</li><li>For each element <var>number</var> of <var>coerced</var>, do<ol><li>If <var>number</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>number</var> is <emu-val>+0</emu-val><sub>𝔽</sub> and <var>highest</var> is <emu-val>-0</emu-val><sub>𝔽</sub>, set <var>highest</var> to <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>number</var> &gt; <var>highest</var>, set <var>highest</var> to <var>number</var>.</li></ol></li><li>Return <var>highest</var>.</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The comparison of values to determine the largest value is done using the <emu-xref aoid="IsLessThan" id="_ref_9523"><a href="#sec-islessthan">IsLessThan</a></emu-xref> algorithm except that <emu-val>+0</emu-val><sub>𝔽</sub> is considered to be larger than <emu-val>-0</emu-val><sub>𝔽</sub>.</p>
      </div></emu-note>
      <p>The <emu-val>"length"</emu-val> property of this function is <emu-val>2</emu-val><sub>𝔽</sub>.</p>
    </emu-clause>

    <emu-clause id="sec-math.min">
      <h1><span class="secnum">21.3.2.25</span> Math.min ( ...<var>args</var> )</h1>
      <p>Given zero or more arguments, this function calls <emu-xref aoid="ToNumber" id="_ref_9524"><a href="#sec-tonumber">ToNumber</a></emu-xref> on each of the arguments and returns the smallest of the resulting values.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>coerced</var> be a new empty <emu-xref href="#sec-list-and-record-specification-type" id="_ref_9525"><a href="#sec-list-and-record-specification-type">List</a></emu-xref>.</li><li>For each element <var>arg</var> of <var>args</var>, do<ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9526"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>arg</var>).</li><li>Append <var>n</var> to <var>coerced</var>.</li></ol></li><li>Let <var>lowest</var> be <emu-val>+∞</emu-val><sub>𝔽</sub>.</li><li>For each element <var>number</var> of <var>coerced</var>, do<ol><li>If <var>number</var> is <emu-val>NaN</emu-val>, return <emu-val>NaN</emu-val>.</li><li>If <var>number</var> is <emu-val>-0</emu-val><sub>𝔽</sub> and <var>lowest</var> is <emu-val>+0</emu-val><sub>𝔽</sub>, set <var>lowest</var> to <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>If <var>number</var> &lt; <var>lowest</var>, set <var>lowest</var> to <var>number</var>.</li></ol></li><li>Return <var>lowest</var>.</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The comparison of values to determine the largest value is done using the <emu-xref aoid="IsLessThan" id="_ref_9527"><a href="#sec-islessthan">IsLessThan</a></emu-xref> algorithm except that <emu-val>+0</emu-val><sub>𝔽</sub> is considered to be larger than <emu-val>-0</emu-val><sub>𝔽</sub>.</p>
      </div></emu-note>
      <p>The <emu-val>"length"</emu-val> property of this function is <emu-val>2</emu-val><sub>𝔽</sub>.</p>
    </emu-clause>

    <emu-clause id="sec-math.pow">
      <h1><span class="secnum">21.3.2.26</span> Math.pow ( <var>base</var>, <var>exponent</var> )</h1>
      <p>This function performs the following steps when called:</p>
      <emu-alg><ol><li>Set <var>base</var> to ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9528"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>base</var>).</li><li>Set <var>exponent</var> to ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9529"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>exponent</var>).</li><li>Return <emu-xref aoid="Number::exponentiate" id="_ref_9530"><a href="#sec-numeric-types-number-exponentiate">Number::exponentiate</a></emu-xref>(<var>base</var>, <var>exponent</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.random">
      <h1><span class="secnum">21.3.2.27</span> Math.random ( )</h1>
      <p>This function returns a Number value with positive sign, greater than or equal to <emu-val>+0</emu-val><sub>𝔽</sub> but strictly less than <emu-val>1</emu-val><sub>𝔽</sub>, chosen randomly or pseudo randomly with approximately uniform distribution over that range, using an <emu-xref href="#implementation-defined" id="_ref_9531"><a href="#implementation-defined">implementation-defined</a></emu-xref> algorithm or strategy.</p>
      <p>Each <code>Math.random</code> function created for distinct <emu-xref href="#realm" id="_ref_9532"><a href="#realm">realms</a></emu-xref> must produce a distinct sequence of values from successive calls.</p>
    </emu-clause>

    <emu-clause id="sec-math.round">
      <h1><span class="secnum">21.3.2.28</span> Math.round ( <var>x</var> )</h1>
      <p>This function returns the Number value that is closest to <var>x</var> and is integral. If two <emu-xref href="#integral-number" id="_ref_9533"><a href="#integral-number">integral Numbers</a></emu-xref> are equally close to <var>x</var>, then the result is the Number value that is closer to +∞. If <var>x</var> is already integral, the result is <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9534"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9535"><a href="#finite">finite</a></emu-xref> or <var>n</var> is an <emu-xref href="#integral-number" id="_ref_9536"><a href="#integral-number">integral Number</a></emu-xref>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>0.5</emu-val><sub>𝔽</sub> and <var>n</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub> and <var>n</var> ≥ <emu-val>-0.5</emu-val><sub>𝔽</sub>, return <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>Return the <emu-xref href="#integral-number" id="_ref_9537"><a href="#integral-number">integral Number</a></emu-xref> closest to <var>n</var>, preferring the Number closer to +∞ in the case of a tie.</li></ol></emu-alg>
      <emu-note><span class="note">Note 1</span><div class="note-contents">
        <p><code>Math.round(3.5)</code> returns 4, but <code>Math.round(-3.5)</code> returns -3.</p>
      </div></emu-note>
      <emu-note><span class="note">Note 2</span><div class="note-contents">
        <p>The value of <code>Math.round(x)</code> is not always the same as the value of <code>Math.floor(x + 0.5)</code>. When <code>x</code> is <emu-val>-0</emu-val><sub>𝔽</sub> or <code>x</code> is less than <emu-val>+0</emu-val><sub>𝔽</sub> but greater than or equal to <emu-val>-0.5</emu-val><sub>𝔽</sub>, <code>Math.round(x)</code> returns <emu-val>-0</emu-val><sub>𝔽</sub>, but <code>Math.floor(x + 0.5)</code> returns <emu-val>+0</emu-val><sub>𝔽</sub>. <code>Math.round(x)</code> may also differ from the value of <code>Math.floor(x + 0.5)</code>because of internal rounding when computing <code>x + 0.5</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.sign">
      <h1><span class="secnum">21.3.2.29</span> Math.sign ( <var>x</var> )</h1>
      <p>This function returns the sign of <var>x</var>, indicating whether <var>x</var> is positive, negative, or zero.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9538"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>-1</emu-val><sub>𝔽</sub>.</li><li>Return <emu-val>1</emu-val><sub>𝔽</sub>.</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.sin">
      <h1><span class="secnum">21.3.2.30</span> Math.sin ( <var>x</var> )</h1>
      <p>This function returns the sine of <var>x</var>. The argument is expressed in radians.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9539"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is either <emu-val>+∞</emu-val><sub>𝔽</sub> or <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9540"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the sine of <emu-xref aoid="ℝ" id="_ref_9541"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.sinh">
      <h1><span class="secnum">21.3.2.31</span> Math.sinh ( <var>x</var> )</h1>
      <p>This function returns the hyperbolic sine of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9542"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9543"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9544"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the hyperbolic sine of <emu-xref aoid="ℝ" id="_ref_9545"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.sinh(x)</code> is the same as the value of <code>(Math.exp(x) - Math.exp(-x)) / 2</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.sqrt">
      <h1><span class="secnum">21.3.2.32</span> Math.sqrt ( <var>x</var> )</h1>
      <p>This function returns the square root of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9546"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, <emu-val>-0</emu-val><sub>𝔽</sub>, or <emu-val>+∞</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9547"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the square root of <emu-xref aoid="ℝ" id="_ref_9548"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.tan">
      <h1><span class="secnum">21.3.2.33</span> Math.tan ( <var>x</var> )</h1>
      <p>This function returns the tangent of <var>x</var>. The argument is expressed in radians.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9549"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is either <emu-val>+∞</emu-val><sub>𝔽</sub> or <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>NaN</emu-val>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9550"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the tangent of <emu-xref aoid="ℝ" id="_ref_9551"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
    </emu-clause>

    <emu-clause id="sec-math.tanh">
      <h1><span class="secnum">21.3.2.34</span> Math.tanh ( <var>x</var> )</h1>
      <p>This function returns the hyperbolic tangent of <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9552"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is one of <emu-val>NaN</emu-val>, <emu-val>+0</emu-val><sub>𝔽</sub>, or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> is <emu-val>+∞</emu-val><sub>𝔽</sub>, return <emu-val>1</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> is <emu-val>-∞</emu-val><sub>𝔽</sub>, return <emu-val>-1</emu-val><sub>𝔽</sub>.</li><li>Return an <emu-xref href="#implementation-approximated" id="_ref_9553"><a href="#implementation-approximated">implementation-approximated</a></emu-xref> Number value representing the result of the hyperbolic tangent of <emu-xref aoid="ℝ" id="_ref_9554"><a href="#ℝ">ℝ</a></emu-xref>(<var>n</var>).</li></ol></emu-alg>
      <emu-note><span class="note">Note</span><div class="note-contents">
        <p>The value of <code>Math.tanh(x)</code> is the same as the value of <code>(Math.exp(x) - Math.exp(-x)) / (Math.exp(x) + Math.exp(-x))</code>.</p>
      </div></emu-note>
    </emu-clause>

    <emu-clause id="sec-math.trunc">
      <h1><span class="secnum">21.3.2.35</span> Math.trunc ( <var>x</var> )</h1>
      <p>This function returns the integral part of the number <var>x</var>, removing any fractional digits. If <var>x</var> is already integral, the result is <var>x</var>.</p>
      <p>It performs the following steps when called:</p>
      <emu-alg><ol><li>Let <var>n</var> be ?&nbsp;<emu-xref aoid="ToNumber" id="_ref_9555"><a href="#sec-tonumber" class="e-user-code">ToNumber</a></emu-xref>(<var>x</var>).</li><li>If <var>n</var> is not <emu-xref href="#finite" id="_ref_9556"><a href="#finite">finite</a></emu-xref> or <var>n</var> is either <emu-val>+0</emu-val><sub>𝔽</sub> or <emu-val>-0</emu-val><sub>𝔽</sub>, return <var>n</var>.</li><li>If <var>n</var> &lt; <emu-val>1</emu-val><sub>𝔽</sub> and <var>n</var> &gt; <emu-val>+0</emu-val><sub>𝔽</sub>, return <emu-val>+0</emu-val><sub>𝔽</sub>.</li><li>If <var>n</var> &lt; <emu-val>-0</emu-val><sub>𝔽</sub> and <var>n</var> &gt; <emu-val>-1</emu-val><sub>𝔽</sub>, return <emu-val>-0</emu-val><sub>𝔽</sub>.</li><li>Return the <emu-xref href="#integral-number" id="_ref_9557"><a href="#integral-number">integral Number</a></emu-xref> nearest <var>n</var> in the direction of <emu-val>+0</emu-val><sub>𝔽</sub>.</li></ol></emu-alg>
    </emu-clause>
  </emu-clause>
</emu-clause>
"""
ECMA262_MATH_OBJECT_SECTIONS = [
    Section(
        url="https://tc39.es/ecma262/#sec-math-object",
        id="sec-math-object",
        number="21.3",
        title="The Math Object",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-value-properties-of-the-math-object",
        id="sec-value-properties-of-the-math-object",
        number="21.3.1",
        title="Value Properties of the Math Object",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.e",
        id="sec-math.e",
        number="21.3.1.1",
        title="Math.E",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.ln10",
        id="sec-math.ln10",
        number="21.3.1.2",
        title="Math.LN10",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.ln2",
        id="sec-math.ln2",
        number="21.3.1.3",
        title="Math.LN2",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log10e",
        id="sec-math.log10e",
        number="21.3.1.4",
        title="Math.LOG10E",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log2e",
        id="sec-math.log2e",
        number="21.3.1.5",
        title="Math.LOG2E",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.pi",
        id="sec-math.pi",
        number="21.3.1.6",
        title="Math.PI",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sqrt1_2",
        id="sec-math.sqrt1_2",
        number="21.3.1.7",
        title="Math.SQRT1_2",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sqrt2",
        id="sec-math.sqrt2",
        number="21.3.1.8",
        title="Math.SQRT2",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math-@@tostringtag",
        id="sec-math-@@tostringtag",
        number="21.3.1.9",
        title="Math [ @@toStringTag ]",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-function-properties-of-the-math-object",
        id="sec-function-properties-of-the-math-object",
        number="21.3.2",
        title="Function Properties of the Math Object",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.abs",
        id="sec-math.abs",
        number="21.3.2.1",
        title="Math.abs ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is NaN, return NaN.",
            "If n is -0𝔽, return +0𝔽.",
            "If n is -∞𝔽, return +∞𝔽.",
            "If n < -0𝔽, return -n.",
            "Return n.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.acos",
        id="sec-math.acos",
        number="21.3.2.2",
        title="Math.acos ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is NaN, n > 1𝔽, or n < -1𝔽, return NaN.",
            "If n is 1𝔽, return +0𝔽.",
            "Return an implementation-approximated Number value representing the result of the inverse cosine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.acosh",
        id="sec-math.acosh",
        number="21.3.2.3",
        title="Math.acosh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is either NaN or +∞𝔽, return n.",
            "If n is 1𝔽, return +0𝔽.",
            "If n < 1𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the inverse hyperbolic cosine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.asin",
        id="sec-math.asin",
        number="21.3.2.4",
        title="Math.asin ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n > 1𝔽 or n < -1𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the inverse sine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.asinh",
        id="sec-math.asinh",
        number="21.3.2.5",
        title="Math.asinh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "Return an implementation-approximated Number value representing the result of the inverse hyperbolic sine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.atan",
        id="sec-math.atan",
        number="21.3.2.6",
        title="Math.atan ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n is +∞𝔽, return an implementation-approximated Number value representing π / 2.",
            "If n is -∞𝔽, return an implementation-approximated Number value representing -π / 2.",
            "Return an implementation-approximated Number value representing the result of the inverse tangent of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.atanh",
        id="sec-math.atanh",
        number="21.3.2.7",
        title="Math.atanh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n > 1𝔽 or n < -1𝔽, return NaN.",
            "If n is 1𝔽, return +∞𝔽.",
            "If n is -1𝔽, return -∞𝔽.",
            "Return an implementation-approximated Number value representing the result of the inverse hyperbolic tangent of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.atan2",
        id="sec-math.atan2",
        number="21.3.2.8",
        title="Math.atan2 ( y, x )",
        algorithm_steps=[
            "Let ny be ? ToNumber(y).",
            "Let nx be ? ToNumber(x).",
            "If ny is NaN or nx is NaN, return NaN.",
            "If ny is +∞𝔽, then",
            [
                "If nx is +∞𝔽, return an "
                "implementation-approximated Number value "
                "representing π / 4.",
                "If nx is -∞𝔽, return an "
                "implementation-approximated Number value "
                "representing 3π / 4.",
                "Return an implementation-approximated Number value "
                "representing π / 2.",
            ],
            "If ny is -∞𝔽, then",
            [
                "If nx is +∞𝔽, return an "
                "implementation-approximated Number value "
                "representing -π / 4.",
                "If nx is -∞𝔽, return an "
                "implementation-approximated Number value "
                "representing -3π / 4.",
                "Return an implementation-approximated Number value "
                "representing -π / 2.",
            ],
            "If ny is +0𝔽, then",
            [
                "If nx > +0𝔽 or nx is +0𝔽, return +0𝔽.",
                "Return an implementation-approximated Number value " "representing π.",
            ],
            "If ny is -0𝔽, then",
            [
                "If nx > +0𝔽 or nx is +0𝔽, return -0𝔽.",
                "Return an implementation-approximated Number value "
                "representing -π.",
            ],
            "Assert: ny is finite and is neither +0𝔽 nor -0𝔽.",
            "If ny > +0𝔽, then",
            [
                "If nx is +∞𝔽, return +0𝔽.",
                "If nx is -∞𝔽, return an "
                "implementation-approximated Number value "
                "representing π.",
                "If nx is either +0𝔽 or -0𝔽, return an "
                "implementation-approximated Number value "
                "representing π / 2.",
            ],
            "If ny < -0𝔽, then",
            [
                "If nx is +∞𝔽, return -0𝔽.",
                "If nx is -∞𝔽, return an "
                "implementation-approximated Number value "
                "representing -π.",
                "If nx is either +0𝔽 or -0𝔽, return an "
                "implementation-approximated Number value "
                "representing -π / 2.",
            ],
            "Assert: nx is finite and is neither +0𝔽 nor -0𝔽.",
            "Return an implementation-approximated Number value representing the result of the inverse tangent of the quotient ℝ(ny) / ℝ(nx).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.cbrt",
        id="sec-math.cbrt",
        number="21.3.2.9",
        title="Math.cbrt ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "Return an implementation-approximated Number value representing the result of the cube root of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.ceil",
        id="sec-math.ceil",
        number="21.3.2.10",
        title="Math.ceil ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "If n < -0𝔽 and n > -1𝔽, return -0𝔽.",
            "If n is an integral Number, return n.",
            "Return the smallest (closest to -∞) integral Number value that is not less than n.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.clz32",
        id="sec-math.clz32",
        number="21.3.2.11",
        title="Math.clz32 ( x )",
        algorithm_steps=[
            "Let n be ? ToUint32(x).",
            "Let p be the number of leading zero bits in the unsigned 32-bit binary representation of n.",
            "Return 𝔽(p).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.cos",
        id="sec-math.cos",
        number="21.3.2.12",
        title="Math.cos ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite, return NaN.",
            "If n is either +0𝔽 or -0𝔽, return 1𝔽.",
            "Return an implementation-approximated Number value representing the result of the cosine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.cosh",
        id="sec-math.cosh",
        number="21.3.2.13",
        title="Math.cosh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is NaN, return NaN.",
            "If n is either +∞𝔽 or -∞𝔽, return +∞𝔽.",
            "If n is either +0𝔽 or -0𝔽, return 1𝔽.",
            "Return an implementation-approximated Number value representing the result of the hyperbolic cosine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.exp",
        id="sec-math.exp",
        number="21.3.2.14",
        title="Math.exp ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is either NaN or +∞𝔽, return n.",
            "If n is either +0𝔽 or -0𝔽, return 1𝔽.",
            "If n is -∞𝔽, return +0𝔽.",
            "Return an implementation-approximated Number value representing the result of the exponential function of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.expm1",
        id="sec-math.expm1",
        number="21.3.2.15",
        title="Math.expm1 ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, -0𝔽, or +∞𝔽, return n.",
            "If n is -∞𝔽, return -1𝔽.",
            "Return an implementation-approximated Number value representing the result of subtracting 1 from the exponential function of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.floor",
        id="sec-math.floor",
        number="21.3.2.16",
        title="Math.floor ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "If n < 1𝔽 and n > +0𝔽, return +0𝔽.",
            "If n is an integral Number, return n.",
            "Return the greatest (closest to +∞) integral Number value that is not greater than n.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.fround",
        id="sec-math.fround",
        number="21.3.2.17",
        title="Math.fround ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is NaN, return NaN.",
            "If n is one of +0𝔽, -0𝔽, +∞𝔽, or -∞𝔽, return n.",
            "Let n32 be the result of converting n to a value in IEEE 754-2019 binary32 format using roundTiesToEven mode.",
            "Let n64 be the result of converting n32 to a value in IEEE 754-2019 binary64 format.",
            "Return the ECMAScript Number value corresponding to " "n64.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.hypot",
        id="sec-math.hypot",
        number="21.3.2.18",
        title="Math.hypot ( ...args )",
        algorithm_steps=[
            "Let coerced be a new empty List.",
            "For each element arg of args, do",
            ["Let n be ? ToNumber(arg).", "Append n to coerced."],
            "For each element number of coerced, do",
            ["If number is either +∞𝔽 or -∞𝔽, return +∞𝔽."],
            "Let onlyZero be true.",
            "For each element number of coerced, do",
            [
                "If number is NaN, return NaN.",
                "If number is neither +0𝔽 nor -0𝔽, set onlyZero to " "false.",
            ],
            "If onlyZero is true, return +0𝔽.",
            "Return an implementation-approximated Number value representing the square root of the sum of squares of the mathematical values of the elements of coerced.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.imul",
        id="sec-math.imul",
        number="21.3.2.19",
        title="Math.imul ( x, y )",
        algorithm_steps=[
            "Let a be ℝ(? ToUint32(x)).",
            "Let b be ℝ(? ToUint32(y)).",
            "Let product be (a × b) modulo 2^32.",
            "If product ≥ 2^31, return 𝔽(product - 2^32); otherwise return 𝔽(product).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log",
        id="sec-math.log",
        number="21.3.2.20",
        title="Math.log ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is either NaN or +∞𝔽, return n.",
            "If n is 1𝔽, return +0𝔽.",
            "If n is either +0𝔽 or -0𝔽, return -∞𝔽.",
            "If n < -0𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the natural logarithm of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log1p",
        id="sec-math.log1p",
        number="21.3.2.21",
        title="Math.log1p ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, -0𝔽, or +∞𝔽, return n.",
            "If n is -1𝔽, return -∞𝔽.",
            "If n < -1𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the natural logarithm of 1 + ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log10",
        id="sec-math.log10",
        number="21.3.2.22",
        title="Math.log10 ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is either NaN or +∞𝔽, return n.",
            "If n is 1𝔽, return +0𝔽.",
            "If n is either +0𝔽 or -0𝔽, return -∞𝔽.",
            "If n < -0𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the base 10 logarithm of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.log2",
        id="sec-math.log2",
        number="21.3.2.23",
        title="Math.log2 ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is either NaN or +∞𝔽, return n.",
            "If n is 1𝔽, return +0𝔽.",
            "If n is either +0𝔽 or -0𝔽, return -∞𝔽.",
            "If n < -0𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the base 2 logarithm of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.max",
        id="sec-math.max",
        number="21.3.2.24",
        title="Math.max ( ...args )",
        algorithm_steps=[
            "Let coerced be a new empty List.",
            "For each element arg of args, do",
            ["Let n be ? ToNumber(arg).", "Append n to coerced."],
            "Let highest be -∞𝔽.",
            "For each element number of coerced, do",
            [
                "If number is NaN, return NaN.",
                "If number is +0𝔽 and highest is -0𝔽, set highest " "to +0𝔽.",
                "If number > highest, set highest to number.",
            ],
            "Return highest.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.min",
        id="sec-math.min",
        number="21.3.2.25",
        title="Math.min ( ...args )",
        algorithm_steps=[
            "Let coerced be a new empty List.",
            "For each element arg of args, do",
            ["Let n be ? ToNumber(arg).", "Append n to coerced."],
            "Let lowest be +∞𝔽.",
            "For each element number of coerced, do",
            [
                "If number is NaN, return NaN.",
                "If number is -0𝔽 and lowest is +0𝔽, set lowest to " "-0𝔽.",
                "If number < lowest, set lowest to number.",
            ],
            "Return lowest.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.pow",
        id="sec-math.pow",
        number="21.3.2.26",
        title="Math.pow ( base, exponent )",
        algorithm_steps=[
            "Set base to ? ToNumber(base).",
            "Set exponent to ? ToNumber(exponent).",
            "Return Number::exponentiate(base, exponent).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.random",
        id="sec-math.random",
        number="21.3.2.27",
        title="Math.random ( )",
        algorithm_steps=[],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.round",
        id="sec-math.round",
        number="21.3.2.28",
        title="Math.round ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is an integral Number, " "return n.",
            "If n < 0.5𝔽 and n > +0𝔽, return +0𝔽.",
            "If n < -0𝔽 and n ≥ -0.5𝔽, return -0𝔽.",
            "Return the integral Number closest to n, preferring the Number closer to +∞ in the case of a tie.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sign",
        id="sec-math.sign",
        number="21.3.2.29",
        title="Math.sign ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n < -0𝔽, return -1𝔽.",
            "Return 1𝔽.",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sin",
        id="sec-math.sin",
        number="21.3.2.30",
        title="Math.sin ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n is either +∞𝔽 or -∞𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the sine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sinh",
        id="sec-math.sinh",
        number="21.3.2.31",
        title="Math.sinh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "Return an implementation-approximated Number value representing the result of the hyperbolic sine of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.sqrt",
        id="sec-math.sqrt",
        number="21.3.2.32",
        title="Math.sqrt ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, -0𝔽, or +∞𝔽, return n.",
            "If n < -0𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the square root of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.tan",
        id="sec-math.tan",
        number="21.3.2.33",
        title="Math.tan ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n is either +∞𝔽 or -∞𝔽, return NaN.",
            "Return an implementation-approximated Number value representing the result of the tangent of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.tanh",
        id="sec-math.tanh",
        number="21.3.2.34",
        title="Math.tanh ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is one of NaN, +0𝔽, or -0𝔽, return n.",
            "If n is +∞𝔽, return 1𝔽.",
            "If n is -∞𝔽, return -1𝔽.",
            "Return an implementation-approximated Number value representing the result of the hyperbolic tangent of ℝ(n).",
        ],
    ),
    Section(
        url="https://tc39.es/ecma262/#sec-math.trunc",
        id="sec-math.trunc",
        number="21.3.2.35",
        title="Math.trunc ( x )",
        algorithm_steps=[
            "Let n be ? ToNumber(x).",
            "If n is not finite or n is either +0𝔽 or -0𝔽, " "return n.",
            "If n < 1𝔽 and n > +0𝔽, return +0𝔽.",
            "If n < -0𝔽 and n > -1𝔽, return -0𝔽.",
            "Return the integral Number nearest n in the " "direction of +0𝔽.",
        ],
    ),
]

# https://tc39.es/proposal-temporal/#sec-temporal-calendardatetoiso
TEMPORAL_CALENDAR_DATE_TO_ISO_HTML = """
<emu-clause id="sec-temporal-calendardatetoiso" type="implementation-defined abstract operation" aoid="CalendarDateToISO">
  <h1><span class="secnum">15.7.1.3</span> CalendarDateToISO ( <var>calendar</var>, <var>fields</var>, <var>overflow</var> )</h1>
  <p>The <emu-xref href="#implementation-defined"><a href="https://tc39.es/ecma262/#implementation-defined">implementation-defined</a></emu-xref> abstract operation CalendarDateToISO takes arguments <var>calendar</var> (a String), <var>fields</var> (an ordinary Object for which the value of the [[Prototype]] internal slot is <emu-val>null</emu-val> and every property is a <emu-xref href="#sec-object-type"><a href="https://tc39.es/ecma262/#sec-object-type">data property</a></emu-xref>), and <var>overflow</var> (<emu-val>"constrain"</emu-val> or <emu-val>"reject"</emu-val>) and returns either a <emu-xref href="#sec-completion-record-specification-type"><a href="https://tc39.es/ecma262/#sec-completion-record-specification-type">normal completion containing</a></emu-xref> an <emu-xref href="#sec-temporal-iso-date-records" id="_ref_1628"><a href="#sec-temporal-iso-date-records">ISO Date Record</a></emu-xref>, or an <emu-xref href="#sec-completion-record-specification-type"><a href="https://tc39.es/ecma262/#sec-completion-record-specification-type">abrupt completion</a></emu-xref>. 
      It performs <emu-xref href="#implementation-defined"><a href="https://tc39.es/ecma262/#implementation-defined">implementation-defined</a></emu-xref> processing to convert <var>fields</var>, which describes a date in the calendar represented by <var>calendar</var>, to the ISO 8601 calendar, subject to processing specified by <var>overflow</var>.
      For <emu-val>"reject"</emu-val>, values that do not form a valid date cause an exception to be thrown, as described below.
      For <emu-val>"constrain"</emu-val>, values that do not form a valid date are clamped to the correct range.
      It then returns an <emu-xref href="#sec-temporal-iso-date-records" id="_ref_1629"><a href="#sec-temporal-iso-date-records">ISO Date Record</a></emu-xref> with the corresponding ISO date.
    </p>
  <p>
    The operation throws a <emu-val>TypeError</emu-val> exception if the properties present on <var>fields</var> are insufficient to identify a unique date in <var>calendar</var>.
    For example, for a <var>calendar</var> that uses eras, a <emu-val>TypeError</emu-val> is thrown if <var>fields</var> does not include any of the following minimum combinations of properties:
  </p>
  <ul>
    <li><emu-val>"year"</emu-val>, <emu-val>"monthCode"</emu-val>, <emu-val>"day"</emu-val></li>
    <li><emu-val>"year"</emu-val>, <emu-val>"month"</emu-val>, <emu-val>"day"</emu-val></li>
    <li><emu-val>"era"</emu-val>, <emu-val>"eraYear"</emu-val>, <emu-val>"monthCode"</emu-val>, <emu-val>"day"</emu-val></li>
    <li><emu-val>"era"</emu-val>, <emu-val>"eraYear"</emu-val>, <emu-val>"month"</emu-val>, <emu-val>"day"</emu-val></li>
  </ul>
  <p>
    The operation throws a <emu-val>RangeError</emu-val> exception if the date described by <var>fields</var> is outside the range allowed by <emu-xref aoid="ISODateTimeWithinLimits" id="_ref_1630"><a href="#sec-temporal-isodatetimewithinlimits">ISODateTimeWithinLimits</a></emu-xref>, or if <var>overflow</var> is <emu-val>"reject"</emu-val> and the date described by <var>fields</var> does not exist.
  </p>
</emu-clause>
"""
TEMPORAL_CALENDAR_DATE_TO_ISO_SECTIONS = [
    Section(
        url="https://tc39.es/ecma262/#sec-temporal-calendardatetoiso",
        id="sec-temporal-calendardatetoiso",
        number="15.7.1.3",
        title="CalendarDateToISO ( calendar, fields, overflow )",
        algorithm_steps=[],
    )
]

# https://tc39.es/proposal-temporal/#sec-temporal-tolocaltime
TEMPORAL_TO_LOCALTIME_HTML = """
<emu-clause id="sec-temporal-tolocaltime" aoid="ToLocalTime">
  <h1><span class="secnum">15.4.22</span> ToLocalTime ( <var>t</var>, <var>calendar</var>, <var>timeZone</var> )</h1>
  <p>
    When the ToLocalTime abstract operation is called with arguments <var>t</var> <ins>(in nanoseconds from the <emu-xref href="#epoch"><a href="https://tc39.es/ecma262/#epoch">epoch</a></emu-xref>)</ins>, <var>calendar</var>, and <var>timeZone</var>, the following steps are taken:
  </p>
  <emu-alg><ol><li><emu-xref href="#assert"><a href="https://tc39.es/ecma262/#assert">Assert</a></emu-xref>: <emu-xref aoid="Type"><a href="https://tc39.es/ecma262/#sec-ecmascript-data-types-and-values">Type</a></emu-xref>(<var>t</var>) is <del>Number</del><ins>BigInt</ins>.</li><li>If <var>calendar</var> is <emu-val>"gregory"</emu-val>, then<ol><li><del>Let <var>timeZoneOffset</var> be the value calculated according to LocalTZA(<var>t</var>, <emu-val>true</emu-val>) where the local time zone is replaced with timezone <var>timeZone</var>.</del></li><li><ins>Let <var>timeZoneOffset</var> be <emu-xref aoid="GetNamedTimeZoneOffsetNanoseconds"><a href="https://tc39.es/ecma262/#sec-getnamedtimezoneoffsetnanoseconds">GetNamedTimeZoneOffsetNanoseconds</a></emu-xref>(<var>timeZone</var>, <var>t</var>).</ins></li><li>Let <var>tz</var> be <del><var>t</var></del><ins><emu-xref aoid="ℝ"><a href="https://tc39.es/ecma262/#ℝ">ℝ</a></emu-xref>(<var>t</var>)</ins> + <var>timeZoneOffset</var>.</li><li>Return a record with fields calculated from <var>tz</var> according to <del><emu-xref href="#table-datetimeformat-tolocaltime-record"><a href="https://tc39.es/ecma402/#table-datetimeformat-tolocaltime-record">Table 7</a></emu-xref></del><ins><emu-xref href="#table-temporal-plaindatetimeformat-tolocaltime-record" id="_ref_60"><a href="#table-temporal-plaindatetimeformat-tolocaltime-record">Table 18</a></emu-xref></ins>.</li></ol></li><li>Else,<ol><li>Return a record with the fields of Column 1 of <del><emu-xref href="#table-datetimeformat-tolocaltime-record"><a href="https://tc39.es/ecma402/#table-datetimeformat-tolocaltime-record">Table 7</a></emu-xref></del><ins><emu-xref href="#table-temporal-plaindatetimeformat-tolocaltime-record" id="_ref_61"><a href="#table-temporal-plaindatetimeformat-tolocaltime-record">Table 18</a></emu-xref></ins> calculated from <del><var>t</var></del><ins><emu-xref aoid="ℝ"><a href="https://tc39.es/ecma262/#ℝ">ℝ</a></emu-xref>(<var>t</var>)</ins> for the given <var>calendar</var> and <var>timeZone</var>. The calculations should use best available information about the specified <var>calendar</var> and <var>timeZone</var>, including current and historical information about time zone offsets from UTC and daylight saving time rules. <ins>Given the same values of <var>t</var>, <var>calendar</var>, and <var>timeZone</var>, the result must be the same for the lifetime of the <emu-xref href="#surrounding-agent"><a href="https://tc39.es/ecma262/#surrounding-agent">surrounding agent</a></emu-xref></ins>.</li></ol></li></ol></emu-alg>
</emu-clause>
"""
TEMPORAL_TO_LOCALTIME_SECTIONS = [
    Section(
        url="https://tc39.es/ecma262/#sec-temporal-tolocaltime",
        id="sec-temporal-tolocaltime",
        number="15.4.22",
        title="ToLocalTime ( t, calendar, timeZone )",
        algorithm_steps=[
            "Assert: Type(t) is BigInt.",
            'If calendar is "gregory", then',
            [
                "Let timeZoneOffset be GetNamedTimeZoneOffsetNanoseconds(timeZone, t).",
                "Let tz be ℝ(t) + timeZoneOffset.",
                "Return a record with fields calculated from tz according to Table 18.",
            ],
            "Else,",
            [
                "Return a record with the fields of Column 1 of Table 18 calculated from ℝ(t) for the given calendar and timeZone. The calculations should use best available information about the specified calendar and timeZone, including current and historical information about time zone offsets from UTC and daylight saving time rules. Given the same values of t, calendar, and timeZone, the result must be the same for the lifetime of the surrounding agent."
            ],
        ],
    ),
]
