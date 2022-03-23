<script lang="ts">
	import Footer from '../../components/Footer.svelte';
import Header from '../../components/Header.svelte';
</script>

<Header />

<div class="p-10 flex justify-center">
	<div class="relative w-4 h-screen bg-gray-900 rounded-3xl" />
	<div
		class="absolute top-40 text-black bg-white z-50 rounded-[100%] w-40 h-40 flex justify-center items-center font-mono text-2xl"
	>
		07.03.2022
	</div>
	<div
		class="absolute top-[32rem] text-black bg-white z-50 rounded-[100%] w-40 h-40 flex justify-center items-center font-mono text-2xl"
	>
		16.03.2022
	</div>
	<div />
</div>

<Footer />