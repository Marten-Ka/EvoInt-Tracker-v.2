<script lang="ts">
	export let img_source: string;
	export let img_alt: string;
	export let heading: string;
	export let content: string;
	export let read_more_link: string;
</script>

<div class="max-w-sm grid grid-rows-2 rounded-lg border shadow-md bg-gray-800 border-gray-700">
	<img class="rounded-t-lg h-full" src={img_source} alt={img_alt} />
	<div class="p-5 grid content-between row-span-2">
		<h5 class="mb-2 text-2xl font-bold tracking-tight text-white">{heading}</h5>
		<p class="mb-3 font-normal text-lg text-gray-300">{content}</p>
		<a
			href={read_more_link}
			class="inline-flex items-center w-fit py-2 px-3 text-sm font-medium text-center text-white rounded-lg focus:ring-4 focus:outline-none bg-blue-600 hover:bg-blue-700 focus:ring-blue-800"
		>
			Read more
			<svg
				class="ml-2 -mr-1 w-4 h-4"
				fill="currentColor"
				viewBox="0 0 20 20"
				xmlns="http://www.w3.org/2000/svg"
				><path
					fill-rule="evenodd"
					d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
					clip-rule="evenodd"
				/></svg
			>
		</a>
	</div>
</div>

<style lang="postcss">
</style>
