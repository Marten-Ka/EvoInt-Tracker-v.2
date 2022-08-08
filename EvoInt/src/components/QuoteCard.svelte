<script lang="ts">
	export let img_link: string;
	export let img_source: string;
	export let img_alt: string;
	export let position: string;
	export let quote: string;
	export let quote_source: string;
	export let author: string;
	export let sub_content: string = '';
</script>

<div class="flex {position}">
	<div class="max-w-4xl xl:max-w-6xl 2xl:max-w-7xl">
		<div class="block p-6 rounded-lg shadow-lg bg-white m-4">
			<div class="md:flex md:flex-row">
				<div
					class="relative group md:w-96 w-36 flex justify-center items-center mb-6 lg:mb-0 mx-auto md:mx-0"
				>
					<img src={img_link} class="rounded-3xl shadow-md" alt={img_alt} />
					<a
						href={img_source}
						target="_blank"
						class="source opacity-0 bottom-0 absolute group-hover:opacity-80 w-full border-[0.5px] rounded-b-3xl overflow-hidden bg-gray-200 text-gray-700 px-6 py-1 text-center"
					>
						©
					</a>
				</div>
				<div class="md:ml-6 place-self-center">
					<p class="text-gray-500 text-base sm:text-lg md:text-xl font-semibold italic mb-6">
						"{quote}"
						<a href={quote_source}><span class="text-blue-500">[*]</span></a>
					</p>
					<p class="font-semibold text-base sm:text-lg md:text-xl mb-2 text-gray-800">{author}</p>
					{#if sub_content}
						<p class="font-semibold text-gray-500 mb-0">{sub_content}</p>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
	@media only screen and (hover: none) and (pointer: coarse) {
		.source {
			opacity: 80;
		}
	}
</style>
